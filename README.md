# ImageMasking
## <U>Introduction</U>
Masking an image with our area of interest is a common approach in geospatial field. However, using heavy apps to perform this simple operation is a time consuming process. So, a user can use this python program to mask a georeferenced image with a user selected shapefile.

## <U>Working</U>
At the first compilation of this program, user is directed to a user interface of this program, with a window, contating four buttons as shown in the figure below:

![rawimage](https://github.com/shresthaasim43/ImageMasking/raw/module1/Assets/First_UI.JPG)

### <U>User guide</U>
This user guide helps you to use the buttons on the user interface shown above for producing the masked image  of your area of interest.
1. <B>Add Image</B>: Press <B>Add Image</B> button to  add the georeferenced image file from your local directory.<br><br>
2. <B>Add Shape file</B>: After pressing this button, you are directed to your local directories, where you shall choose the area of intrest(AOI) of your project  in ".shp format"<br><br>
3. <B>Mask Image</B>: This button when pressed, masks the input image with AOI and saves the masked image to the user selected directory. <br><br>
4. <B>Compare Image</B>:  Click this button to visualize the user input image, masking shapefile of AOI overlayed in it on the first subplot and the masked image in the next subplot area. A image of the plot is shown below:

