import pytesseract
import PIL
import PIL.IcoImagePlugin
import PIL.Image
import matplotlib.pyplot as plt
import cv2
import os

# Set the location of Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Robert\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Constants
file_extension = '.JPEG'
CONFIG = 'l eng — oem 1 — psm 3'

def read_image(file_name):
    """Read and return the image from the specified file."""
    img = cv2.imread(file_name)
    print('.....file read')
    return img

def extract_text_from_image(img):
    """Extract and clean text from the given image using Tesseract OCR."""
    text = pytesseract.image_to_string(img, config=CONFIG)
    if " " in text:
        text = text.replace(" ", "_")
    return text.strip()

def display_image_with_message(file_name, message):
    """Display the image with a message using Matplotlib."""
    with PIL.Image.open(file_name) as pil_img:
        out_img = pil_img.resize((256, 256), PIL.Image.LANCZOS)
        plt.figure(figsize=(6, 6))
        plt.tight_layout()
        plt.rc(('xtick', 'ytick'), color=(1, 1, 1, 0))
        plt.subplot(2, 1, 1)
        plt.imshow(out_img)
        plt.xlabel(message)
        plt.show()

def rename_file(file_name, new_name):
    """Rename the file to the new name."""
    try:
        os.rename(file_name, new_name)
        print('\n\nFile renamed. Moving on.')
    except Exception as e:
        print('\n\nThere was an error renaming the file')
        print(e)

def process_files():
    """Loop through all the files in the directory and process them."""
    try:
        for num in range(3, 68):
            file_name = "Shirt {}.JPEG".format(num)
            print('\nReading file: {}'.format(file_name))
            img = read_image(file_name)
            text = extract_text_from_image(img)
            new_name = 'gildan_softstyle_color_{}'.format(text.lower()) + file_extension
            message = file_name + " will be changed to " + new_name

            display_image_with_message(file_name, message)

            choice = input('\nIs this OK?\n')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                rename_file(file_name, new_name)
            else:
                correct = False
                while not correct:
                    user_renamed = input('\n\nWhat would you like to rename the file?\nDo not include the file extension.(.exe/.jpg/.JPEG) ')
                    if '.' not in user_renamed:
                        new_name = 'gildan_softstyle_color_' + user_renamed.lower() + file_extension
                        choice = input('\nFile will be renamed {}\nIs this OK?(yes/no)\n'.format(new_name))
                        if choice.lower() == 'y' or choice.lower() == 'yes':
                            correct = True
                rename_file(file_name, new_name)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    process_files()
    print('\n\n\t\tThat is all!\n\nGoodbye!')
