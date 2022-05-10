from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import askopenfilename, asksaveasfilename

from functools import partial
import matplotlib
import matplotlib.pyplot as plt

import fiona
import rasterio
import rasterio.mask
from rasterio.plot import show

import numpy as np

W,H = 45 0,200

WINDOW = Tk()
WINDOW.geometry('+10+10') #window starting from 10,10
WINDOW.geometry('{}x{}'.format(W,H)) #set the geomentry of WINDOW
WINDOW.title("Image Masking") 


style = Style()  
style.configure('W.TButton', font =('calibri', 12, 'bold', 'underline'), 
               foreground = 'blue', borderwidth = '4', height=5, width=15) 

def openImage():
    global tif_filePath, tif_fileName
    tif_filePath = askopenfilename(initialdir = "/",title = "Select file",
                        filetypes = (("tif images","*.tif"),("all files","*.*")))
    temp2 = tif_filePath.split('/')[-1]
    tif_fileName = temp2.split('.')[0]
    label1 = Label(WINDOW, text = tif_filePath).place(x = 150, y = 15)

    
def openShp():
    global shapeFilepath, shapeFileName
    shapeFilepath =  askopenfilename(initialdir = "",title = "Select file",
                        filetypes = (("all files","*.*"),("tif images","*.tif")))
    temp = shapeFilepath.split('/')[-1]
    shapeFileName = temp.split('.')[0]
    
    label2= Label(WINDOW, text = shapeFilepath).place(x = 150, y = 50)

def maskImage():
    global clippedImage
    saveFilePath = asksaveasfilename()
    if '.tif' not in saveFilePath:
        saveFilePath += '.tif'

    with fiona.open(shapeFilepath)as shapefile:
        shapes=[feature["geometry"] for feature in shapefile]

    with rasterio.open(tif_filePath) as src:
        out_image,out_transform=rasterio.mask.mask(src,shapes,crop=True)
        out_meta=src.meta
        clippedImage=out_image
     
    out_meta.update({"driver": "GTiff","height": out_image.shape[1],"width": out_image.shape[2],"transform": out_transform})
    with rasterio.open(saveFilePath, "w", **out_meta) as dest:
        dest.write(out_image)


def plotImages():
    fig = plt.figure(figsize=(10, 7))
    # setting values to rows and column variables
    rows = 1
    columns = 2
    
    # reading images
    #Image1 = rasterio.open(tif_filePath).read(1)
    #Image2 = rasterio.open("C:\Users\Bijay\Desktop\Py'\mas.tif").read(1)
    
    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, 1)
    # showing image
    plt.imshow(Image1)
    plt.axis('off')
    plt.title("Unclipped Image")
   
    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, 2)
    
    # showing image
    plt.imshow(Image1)
    plt.axis('off')
    plt.title("Clipped Image")
    

BUTTON_CANVAS = Canvas(WINDOW,width=W,height=H)
BUTTON_CANVAS.place(x=1,y=1, anchor=NW)
btn_rect = BUTTON_CANVAS.create_rectangle(5,5,W-5,H-5)

imageButton = Button(WINDOW,text='Add Image',style='W.TButton',command=openImage)
imageButton.place(x=10,y=10)

shpButton = Button(WINDOW,text='Add shape file',style='W.TButton',command=openShp)
shpButton.place(x=10,y=50)

calculate_btn = Button(WINDOW,text='Mask Image',style='W.TButton',command=maskImage,state="DISABLED")
calculate_btn.place(x=10,y=100)

compare_btn = Button(WINDOW,text='Compare Images',style='W.TButton',command=plotImages, state="DISABLED")
compare_btn.place(x=10,y=150)

WINDOW.mainloop()


