import os
import base64
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to download images
def download_images():
    global download_folder
    if not download_folder:
        status_label.config(text="Please select a download folder")
        return
    
    # Create a new instance of the Chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the Chrome browser and navigate to Bing Images
    driver.get("https://www.bing.com/images")
    
    search_bar = driver.find_element(By.NAME, "q")
    search_term = search_entry.get()
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)  # Press Enter to initiate the search
    
    # Maximum number of images to download
    max_images_to_download = int(max_images_entry.get())
    
    # Keep track of the number of downloaded images
    num_images_downloaded = 0
    
    while num_images_downloaded < max_images_to_download:
        # Scroll down to load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for images to load
        
        # Find image elements and download them
        image_elements = driver.find_elements(By.CLASS_NAME, "mimg")
        for img_element in image_elements:
            img_url = img_element.get_attribute("src")
            if img_url:
                # Check if it's a data URL
                if img_url.startswith("data:image/jpeg;base64,"):
                    # Extract Base64-encoded image data
                    base64_image_data = img_url.split(",")[1]
                    image_data = base64.b64decode(base64_image_data)
                else:
                    # Regular image URL
                    response = requests.get(img_url)
                    
                    # Check if the response content type is an image
                    if 'image' not in response.headers['content-type']:
                        continue  # Skip this iteration if not an image
                    
                    image_data = response.content
    
                # Save the image to the download folder
                img_filename = os.path.join(download_folder, f"image_{num_images_downloaded + 1}.jpeg")
                with open(img_filename, "wb") as img_file:
                    img_file.write(image_data)
    
                num_images_downloaded += 1
                status_label.config(text=f"Downloaded {num_images_downloaded}/{max_images_to_download} images")
                
                if num_images_downloaded >= max_images_to_download:
                    break
    
    # Close the browser
    driver.quit()

# Function to select download folder
def select_folder():
    global download_folder
    download_folder = filedialog.askdirectory()
    if download_folder:
        folder_name = os.path.basename(download_folder)
        folder_label.config(text=f"Download Folder: {folder_name}")

# Create the main window
root = tk.Tk()
root.title("Dataset Maker")

# Set initial window dimensions
window_width = 900
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Make the window non-resizable
root.resizable(False, False)

# Create left and right containers
left_container = tk.Frame(root)
left_container.pack(side="left", padx=10, pady=10)

right_container = tk.Frame(root)
right_container.pack(side="right", padx=10, pady=10)

# Widgets for left container
search_label = tk.Label(left_container, text="Search Term:", font=("Arial", 12), anchor="w")
search_label.pack(anchor="w", pady=(0, 5))

search_entry = tk.Entry(left_container)
search_entry.pack(anchor="w", pady=(0, 5))

max_images_label = tk.Label(left_container, text="Images to Download:", font=("Arial", 12), anchor="w")
max_images_label.pack(anchor="w", pady=(0, 5))

max_images_entry = tk.Entry(left_container)
max_images_entry.pack(anchor="w", pady=(0, 5))

folder_button = tk.Button(left_container, text="Select Download Folder", command=select_folder, font=("Arial", 12))
folder_button.pack(anchor="w", pady=(0, 5))

folder_label = tk.Label(left_container, text="Download Folder: Not Selected", font=("Arial", 12), anchor="w")
folder_label.pack(anchor="w", pady=(0, 35))

download_button = tk.Button(left_container, text="Create Dataset", command=download_images, font=("Arial", 12))
download_button.pack(anchor="w", pady=(0, 10))

status_label = tk.Label(left_container, text="", font=("Arial", 12), anchor="w")
status_label.pack(anchor="w")

# Image for right container
sample_image = Image.open(r"Image_Dataset_generator\assets\image.png")
sample_image = sample_image.resize((600, 400), Image.ANTIALIAS)
sample_image = ImageTk.PhotoImage(sample_image)

image_label = tk.Label(right_container, image=sample_image)
image_label.image = sample_image
image_label.pack()

# Start the main loop
root.mainloop()
