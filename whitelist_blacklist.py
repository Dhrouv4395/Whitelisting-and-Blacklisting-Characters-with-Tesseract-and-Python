#import necessary packages
import pytesseract
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#construct argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument('-i','--input',required=True,help='Path to input image')
ap.add_argument('-w','--whitelist',type=str,default='',help='list of character to whitelist')
ap.add_argument('-b','--blacklist',type=str,default='',help='list of character to blacklist')
args = vars(ap.parse_args())

#load the input image, swap channel ordering and initialize our tesseract 
#OCR option as an empty string

image = cv2.imread(args['input'])
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
options = ""

#check to see if a set of whitelist character has been provided,
# and if so, update our options string
if len(args['whitelist']) > 0:
    options += '-c tessedit_char_whitelist={}'.format(args['whitelist']) 

#check to see if a set of blacklist charcater has been provided,
#and if so, update our option string
if len(args['blacklist']) > 0:
    options += '-c tessedit_char_blacklist={}'.format(args['blacklist'])

#OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)