
# Image Dataset Maker

A simple Python application that allows you to search and download images from Bing Images using Selenium and Tkinter.

## Features

- Search for images based on a given search term in Chrome.
- Specify the number of images to download.
- Creates an easy-made dataset of images.

## UI

![Screenshot](screenshots/screenshot.png)

## Requirements

- Python 3.9.13
- [Selenium](https://pypi.org/project/selenium/)
- [Chrome WebDriver](https://chromedriver.chromium.org/downloads) (Ensure compatibility with your Chrome browser version)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/)

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/UdaySMukherjee/Image-Dataset-Generator.git
   ```
2. Install the required libraries:

   ```sh
   pip install -r requirements.txt
   ```
3. Download the Chrome WebDriver and make sure it's in your system's PATH.

4. Create a blank folder where u would like to store the images

## Usage
1. Run the application:
   ```sh
   python app.py
   ```
2. Enter a search term and the number of images to download.

3. Click the "Select Download Folder" button to choose a download location.

4. Click the "Create Dataset" button to start downloading images for your dataset.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
