#improting the libraries
from PIL import Image
import pytrsseract as pt
import os

def main():
  #Folder path where images are stored
  filepath = r'filepath'
  
  #Folder path where text file will be stored after extraction
  textpath = r'textpath'
  
  #iterating the images in the folder
  for imgName in os.listdir(fiepath):
    inpath = os.path.join(filepath, imgName)
    image = Image.open(inpath)
    
    #Applying OCR using pytesseract
    text = pt.image_to_string(image, lang="eng")
    
    fullPath = os.path.join(textpath, 'time_'+imgName+'.txt')
    #print(text)
    
    # saving the textfor every image in a seperate .txt file
    fileName = open(fullPath, "w")
    fileName.write(text)
    fileName.close()
    
    if __name__ == '__main__':
      main()
