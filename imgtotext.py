import tesseract
import os
from PIL import Image


def convert():
    img = Image.open('Python Projects\IvV2y.png')
    text = tesseract.image_to_string(img)
    print(text)
    
convert()
    
