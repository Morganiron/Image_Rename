import pytesseract
import PIL
import PIL.IcoImagePlugin
import PIL.Image
import matplotlib.pyplot as plt
import cv2
import os

## location of tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Robert\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

file_extension = '.JPEG'

try:
    for num in range(3,68):
        file_name = "Shirt {}.JPEG".format(num)
        print('\nReading file: {}'.format(file_name))
        img = cv2.imread(file_name)
        print('.....file read')

        

        #config
        config=('l eng — oem 1 — psm 3')

        #read text
        text = pytesseract.image_to_string(img, config=config)
        if " " in text:
            text = text.replace(" ", "_")
            text = text.strip()

        new_name = 'gildan_softstyle_color_{}'.format(text.lower())
        new_name = new_name.strip()
        message = file_name + " will be changed to " + new_name + '.JPEG'

        with PIL.Image.open(file_name) as pil_img:
            out_img = pil_img.resize((256, 256), PIL.Image.LANCZOS)

            plt.figure(figsize=(6, 6))
            plt.tight_layout()
            plt.rc(('xtick', 'ytick'), color=(1, 1, 1, 0))
            plt.subplot(2, 1, 1), plt.imshow(out_img)
            plt.xlabel(message)
            plt.show()

        print(message)
        choice = input('\nIs this OK?\n')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            try:
                os.rename(file_name, new_name+file_extension)
            except Exception as e:
                print('\n\nThere was an error renaming the file')
                print(e)
        else:
            correct = False
            while not correct:
                user_renamed = input('\n\nWhat would you like to rename the file?\nDo not include the file extension.(.exe/.jpg/.JPEG) ')

                if '.' not in user_renamed:
                    new_name = 'gildan_softstyle_color_' + user_renamed.lower() + file_extension
                    new_name = new_name.strip()

                    choice = input('\nFile will be renamed {}\nIs this OK?(yes/no)\n'.format(new_name))

                    if choice.lower() == 'y' or choice.lower() == 'yes':
                        correct = True

            try:
                os.rename(file_name, new_name)

            except Exception as e:
                print('\n\nSomething went wrong.\n')
                print(e)


        print('\n\nFile renamed. Moving on.')
        
except Exception as e:
    print(e)

print('\n\n\t\tThat is all!\n\nGoodbye!')



