#Libraries required for the given operation
import pytesseract as pt
from PIL import Image

#Importing the image using Pillow
image = Image.open(r'filename') #It is always good to provide the full path of the image as a raw string, afterall you might never know why it dosen't compile :)
text = pt.image_to_string(image)
print(text)
