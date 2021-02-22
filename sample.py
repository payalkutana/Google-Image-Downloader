from google_images_download import google_images_download   #importing the library
import cv2 as cv
from PIL import Image
import imutils
import os

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"universe,apple","limit":20,"print_urls":True,"format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function


path_DIR="/home/ubuntu/webScraping/google-images-download/downloads"
for img_dir in os.listdir(path_DIR):
    
    for filename in os.listdir(path_DIR+"/"+img_dir):
        #print(filename)
        
        file_path=path_DIR+"/"+img_dir+"/"+filename
        #print(file_path)

        try :
            with Image.open(file_path) as im:
                #print('ok')
                #im=Image.resize(220,180)  Not working
                img = cv.imread(file_path)
                img=cv.resize(img,(250,250),interpolation=cv.INTER_AREA)
                #img = imutils.resize(img, width=300)
                gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                file_name2=path_DIR+"/"+img_dir+"/grayResized_"+filename
                cv.imwrite(file_name2,gray)
        except :
            print(file_path)
            os.remove(file_path)
        


#cv.imshow('Cat',img)

#Converting image to grayscale
#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)
