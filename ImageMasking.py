from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import askopenfilename, asksaveasfilename


  
# This method will show image in any image view
from functools import partial
import matplotlib
import matplotlib.pyplot as plt

import fiona
import rasterio
import rasterio.mask
from rasterio.plot import show
from descartes import PolygonPatch

import numpy as np

W,H = 450,200

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
    global shapeFilePath, shapeFileName
    shapeFilePath =  askopenfilename(initialdir = "",title = "Select file",
                        filetypes = (("all files","*.*"),("tif images","*.tif")))
    temp = shapeFilePath.split('/')[-1]
    shapeFileName = temp.split('.')[0]
    
    label2= Label(WINDOW, text = shapeFilePath).place(x = 150, y = 50)

def maskImage():
    global saveFilePath
    saveFilePath = asksaveasfilename()
    if '.tif' not in saveFilePath:
        saveFilePath += '.tif'

    with fiona.open(shapeFilePath)as shapefile:
        shapes=[feature["geometry"] for feature in shapefile]

    with rasterio.open(tif_filePath) as src:
        out_image,out_transform=rasterio.mask.mask(src,shapes,crop=True)
        out_meta=src.meta
        clippedImage=out_image
     
    out_meta.update({"driver": "GTiff","height": out_image.shape[1],"width": out_image.shape[2],"transform": out_transform})
    with rasterio.open(saveFilePath, "w", **out_meta) as dest:
        dest.write(out_image)


def plotImages():
    image1=rasterio.open(tif_filePath) 
    #image1.show()
    image2=rasterio.open(saveFilePath)
    #image2.show()
    with fiona.open(shapeFilePath, "r") as shapefile:
        features = [feature["geometry"] for feature in shapefile]
    
    patches = [PolygonPatch(feature, edgecolor="red", facecolor="none", linewidth=2) for feature in features]
   
    
    fig, (axr, axg) = plt.subplots(1,2, figsize=(21,7))
    show((image1, 1), ax=axr, title='Unmasked imagery and shape file')
    show((image2, 1), ax=axg, title='Masked Imagery')
    axr.add_collection(matplotlib.collections.PatchCollection(patches,match_original=True))
    
    plt.show()
    

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


