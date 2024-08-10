# Image Text Reader and Renamer

This is a simple Python project that uses OpenCV and Tesseract OCR to read text from images and rename the files accordingly. I created this application to help a friend with naming images for an e-commerce page. The images were stock photos of t-shirts, each in a different color, with the color name displayed under the image. This tool automates the process of renaming each image based on the color name detected in the image.

## Features

- **Text Extraction**: Uses Tesseract OCR to extract text from images.
- **File Renaming**: Automatically renames image files based on the extracted text, with the extracted text as the new file name.
- **User Interaction**: Displays the image and proposed new name, allowing the user to confirm or provide a custom name.
- **Image Resizing**: Resizes images for display purposes during the renaming process.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Tesseract-OCR
- Pillow (`PIL`)
- Tkinter (built-in with Python, no separate installation needed)

## Installation

1. **Install Python**: Make sure you have Python 3 installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Tesseract OCR**:
   - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - During installation, ensure that Tesseract is added to your system's PATH.
   - If not added to PATH, update the `pytesseract.pytesseract.tesseract_cmd` variable in the script with the correct path to the `tesseract.exe` on your system.

3. **Install Python Packages**:
   ```bash
   pip install opencv-python
   pip install pillow
   pip install pytesseract

## Usage

1. **Place Images**: Ensure that your images are in a directory you can easily select during the script execution. The script now dynamically handles different image file extensions (e.g., `.jpeg`, `.jpg`, `.png`, etc.).

2. **Run the Script**: Execute the Python script in your terminal or IDE:
   ```bash
   python image_text_reader.py

3. **Follow Prompts**:

   - A GUI window will appear, allowing you to select the directory containing your images.
   - The script will loop through each image in the selected directory, display it, and propose a new name based on the detected text. You can confirm or provide a custom name.

4. **Renaming**:

   - Once confirmed, the image file will be renamed, and the script will move on to the next image.

## Example

Here's how the script processes an image:

- **Original File Name**: `Shirt 3.JPEG`
- **Detected Text**: `Red`
- **Proposed New Name**: `red.JPEG`

If you confirm the proposed name, the file will be renamed accordingly. If not, you can enter a custom name.

## Notes

- The script processes images with extensions `.jpeg`, `.jpg`, `.png`, `.bmp`, `.tiff`, and `.gif`.
- Ensure that the text in the images is clear for better OCR accuracy.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- **OpenCV** - Computer Vision library used for image processing.
- **Tesseract OCR** - OCR engine used for text extraction.
- **Pillow** - Imaging library used for image manipulation.
- **Tkinter** - Built-in Python library used for GUI development.

### README Updates

#### Version 1.1
- **Updated Installation Instructions**: Added detailed steps for installing Tesseract OCR, including how to set the correct executable path in the script.
- **Simplified Usage Instructions**: Revised the usage instructions to reflect the new GUI-based directory selection and dynamic image file handling.
- **Removed References to Static Prefix**: Updated the examples and descriptions to reflect that the script now uses the extracted text directly as the file name without a static prefix.
- **Added Acknowledgments**: Included acknowledgments for the libraries used in the project, such as OpenCV, Tesseract OCR, Pillow, and Tkinter.
