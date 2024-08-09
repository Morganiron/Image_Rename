# Image Text Reader and Renamer

This is a simple Python project that uses OpenCV and Tesseract OCR to read text from images and rename the files accordingly. I created this application to help a friend with naming images for an e-commerce page. The images were stock photos of t-shirts, each in a different color, with the color name displayed under the image. This tool automates the process of renaming each image based on the color name detected in the image.

## Features

- **Text Extraction**: Uses Tesseract OCR to extract text from images.
- **File Renaming**: Automatically renames image files based on the extracted text.
- **User Interaction**: Displays the image and proposed new name, allowing the user to confirm or provide a custom name.
- **Image Resizing**: Resizes images for display purposes during the renaming process.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Tesseract-OCR
- Pillow (`PIL`)
- Matplotlib

## Installation

1. **Install Python**: Make sure you have Python 3 installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Tesseract**: Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract). After installation, make sure to update the `pytesseract.pytesseract.tesseract_cmd` variable in the script with the correct path to the `tesseract.exe` on your system.

3. **Install Python Packages**:
   ```bash
   pip install opencv-python
   pip install pillow
   pip install matplotlib
   pip install pytesseract
   
## Usage

1. **Place Images**: Ensure that your images are in the same directory as the script. The images should be named sequentially, such as `Shirt 3.JPEG`, `Shirt 4.JPEG`, etc.

2. **Run the Script**: Execute the Python script in your terminal or IDE:
   ```bash
   python image_text_reader.py
   
3. **Follow Prompts**: The script will loop through each image, display it, and propose a new name based on the detected text. You can confirm or provide a custom name.

4. **Renaming**: Once confirmed, the image file will be renamed, and the script will move on to the next image.

## Example

Here's how the script processes an image:

- **Original File Name**: `Shirt 3.JPEG`
- **Detected Text**: `Red`
- **Proposed New Name**: `gildan_softstyle_color_red.JPEG`

If you confirm the proposed name, the file will be renamed accordingly. If not, you can enter a custom name.

## Notes

- The script assumes that the images are in `.JPEG` format. You can modify the `file_extension` variable in the script if you're using a different format.
- Ensure that the text in the images is clear for better OCR accuracy.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- **[OpenCV](https://opencv.org/)** - Computer Vision library used for image processing.
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** - OCR engine used for text extraction.
- **[Pillow](https://python-pillow.org/)** - Imaging library used for image manipulation.
- **[Matplotlib](https://matplotlib.org/)** - Library used for displaying images and text.

