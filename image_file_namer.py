import sys
import os
import cv2
import pytesseract
from PIL import Image, ImageTk, UnidentifiedImageError
from tkinter import Tk, Label, Button, simpledialog, messagebox
from tkinter.filedialog import askdirectory

# Dynamically set the location of the Tesseract executable
tesseract_path = os.path.join(os.path.dirname(__file__), 'tesseract-ocr', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Constants
IMAGE_EXTENSIONS = ('.jpeg', '.jpg', '.png', '.bmp', '.tiff', '.gif')  # List of supported image file extensions
CONFIG = 'l eng — oem 1 — psm 3'

def read_image(file_name):
    """Read and return the image from the specified file."""
    try:
        img = cv2.imread(file_name)
        if img is None:
            raise ValueError(f"Failed to read {file_name}. Skipping.")
        print('.....file read')
        return img
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def extract_text_from_image(img):
    """Extract and clean text from the given image using Tesseract OCR."""
    try:
        text = pytesseract.image_to_string(img, config=CONFIG)
        if " " in text:
            text = text.replace(" ", "_")
        return text.strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from image. {str(e)}")
        return None

def display_image_with_message(root, image, message, confirm_callback, reject_callback):
    """Display the image with a message and confirmation buttons in the root Tkinter window."""
    try:
        root.title("Confirm Rename")
        
        # Clear the root window
        for widget in root.winfo_children():
            widget.destroy()
        
        # Display the message
        label = Label(root, text=message, padx=10, pady=10)
        label.pack()
        
        # Convert the PIL image to a format Tkinter can use
        resized_image = image.resize((256, 256), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        
        # Display the image
        img_label = Label(root, image=tk_image)
        img_label.image = tk_image  # Keep a reference to avoid garbage collection
        img_label.pack()

        # Add Yes and No buttons
        yes_button = Button(root, text="Yes", command=lambda: [confirm_callback(), root.quit()])
        no_button = Button(root, text="No", command=lambda: [reject_callback(), root.quit()])
        yes_button.pack(side="left", padx=10, pady=10)
        no_button.pack(side="right", padx=10, pady=10)

        root.mainloop()
    except UnidentifiedImageError:
        messagebox.showerror("Error", "Failed to process the image. The image file may be corrupted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def rename_file(old_name, new_name):
    """Rename the file to the new name."""
    try:
        os.rename(old_name, new_name)
        print('\n\nFile renamed. Moving on.')
    except Exception as e:
        messagebox.showerror("Error", f"There was an error renaming the file: {str(e)}")

def get_user_input(prompt):
    """Prompt the user for input using a simple dialog."""
    try:
        user_input = simple
