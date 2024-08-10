import sys
import os
import cv2
import pytesseract
from PIL import Image, ImageTk, UnidentifiedImageError
from tkinter import Tk, Label, Button, simpledialog, messagebox
from tkinter.filedialog import askdirectory

# Hard-code the path to the Tesseract executable
# Python cannot find it without a static path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
        print(f'File renamed to {new_name}')
    except Exception as e:
        messagebox.showerror("Error", f"There was an error renaming the file: {str(e)}")

def get_user_input(prompt):
    """Prompt the user for input using a simple dialog."""
    try:
        user_input = simpledialog.askstring("Input Required", prompt)
        return user_input
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get user input: {str(e)}")
        return None

def on_reject(full_path, new_name, directory, file_name):
    """Handle the rejection case when the user chooses not to rename the file with the proposed name."""
    user_input = get_user_input('What would you like to rename the file to? (Do not include file extension):')
    if user_input and '.' not in user_input:
        new_new_name = os.path.join(directory, f'{user_input.lower()}{os.path.splitext(file_name)[1]}')
        if confirm_rename(f'File will be renamed to {os.path.basename(new_new_name)}. Is this OK?'):
            rename_file(full_path, new_new_name)
    elif user_input is None:  # User pressed "Cancel"
        messagebox.showinfo("No Change", "The file name will not be changed.")

def confirm_rename(message):
    """Display a confirmation dialog with Yes/No buttons."""
    try:
        result = messagebox.askyesno("Confirm Rename", message)
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Failed to confirm rename: {str(e)}")
        return False

def open_directory_selection():
    """Open the directory selection dialog and start processing files."""
    try:
        directory = askdirectory(title="Select Directory Containing Images")
        if directory:
            process_files(directory)
        else:
            print("No directory selected. Exiting.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open directory selection: {str(e)}")

def process_files(directory):
    """Loop through all supported image files in the directory and process them."""
    try:
        for file_name in os.listdir(directory):
            if file_name.lower().endswith(IMAGE_EXTENSIONS):
                full_path = os.path.join(directory, file_name)
                print('\nReading file: {}'.format(full_path))
                
                img = read_image(full_path)
                if img is None:
                    continue  # Skip to the next file if reading failed
                
                text = extract_text_from_image(img)
                if not text:
                    continue  # Skip to the next file if text extraction failed
                
                new_name = os.path.join(directory, f'{text.lower()}{os.path.splitext(file_name)[1]}')
                message = f'{file_name}\nwill be changed to\n{os.path.basename(new_name)}'

                with Image.open(full_path) as pil_img:
                    def on_confirm():
                        rename_file(full_path, new_name)
                    
                    display_image_with_message(root, pil_img, message, on_confirm, lambda: on_reject(full_path, new_name, directory, file_name))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing files: {str(e)}")
        
if __name__ == "__main__":
    # Create the root window
    root = Tk()
    root.withdraw()  # Hide the root window initially
    
    # Create the introduction window in the root
    root.deiconify()  # Show the root window
    root.title("Image Text Reader and Renamer")
    
    # Create a label with the introduction text
    intro_label = Label(root, text="Welcome to the Image Text Reader and Renamer Application!\n\nThis application reads text from images and renames the images based on the detected text.", padx=20, pady=20)
    intro_label.pack()

    # Create a button to select the directory and start processing
    select_button = Button(root, text="Select Directory and Start", command=open_directory_selection, padx=10, pady=5)
    select_button.pack(pady=20)

    # Run the Tkinter main loop
    root.mainloop()

    # Once the directory is selected, the rest of the script runs.
    try:
        pass  # The process_files function will be called inside open_directory_selection
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    finally:
        print('\n\n\t\tThat is all!\n\nGoodbye!')
