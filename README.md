# ImageMasking
## <U>Introduction</U>
Masking an image with our area of interest is a common approach in geospatial field. However, using heavy apps to perform this simple operation is a time consuming process. So, a user can use this python program to mask a georeferenced image with a user selected shapefile.

## <U>Working</U>
At first compilation of this program, user is directed to a user interface of this program, with a window, contating four buttons as shown in the figure below:

![rawimage](https://github.com/shresthaasim43/ImageMasking/raw/module1/Assets/First_UI.JPG)

### <U>User guide</U>
This user guide helps you to use the buttons on the user interface shown above for producing the masked image  of your area of interest.
1. <B>Add Image</B>: Press <B>Add Image</B> button to  add the georeferenced image file from your local directory.<br><br>
2. <B>Add Shape file</B>: After pressing this button, you are directed to your local directories, where you shall choose the area of intrest(AOI) of your project  in ".shp format"<br><br>
3. <B>Mask Image</B>: This button when pressed, masks the input image with AOI and saves the masked image to the user selected directory. <B>Masked Successfully</B> will be labelled to the right of this button after the task is completed. <B><br>
4. <B>Plot Results</B>:  Click this button to visualize the user input image, masking shapefile of AOI overlayed on it, and the masked image in two subplot area. Snapshot of the plot is shown below:
![rawimage](https://github.com/shresthaasim43/ImageMasking/raw/module1/Assets/Visualization.JPG)
 Futher a video, showing the working of this program is demonstrated below for better understanding:
![rawimage](https://github.com/shresthaasim43/ImageMasking/raw/module1/Assets/Manual.gif)



