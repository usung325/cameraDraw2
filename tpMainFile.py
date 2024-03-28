from cmu_graphics import *
import cv2 as cv
from PIL import Image, ImageDraw
import os, pathlib
from classBeta import * # All Classes
from classBucket import *
from os import listdir
from os.path import isfile, join

# from classBucketBeta import *

# For more information on image modes in PIL,
# See: https://pillow.readthedocs.io/en/stable/handbook/concepts.html
# This one is from the tech demo on Piazza

def initFileSys(app):
    app.allFiles = [f for f in listdir("/Users/roy/Downloads/@yoosung_design/S24 Capstone/cameraDraw/submissions") if isfile(join("/Users/roy/Downloads/@yoosung_design/S24 Capstone/cameraDraw/submissions", f))]

def fileSysAppend(app, name):
    app.allFiles.append(f'{name}.png')

def drawSubmissions(app):
    app.reversedAllFiles = app.allFiles[::-1]
    


def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def initializeDict(app):
    # dictionary to store if the pixel's been activated or not. 
    app.pixelData = dict()

    # For now, initialize dictionary with all xy coords as "False"
    for x in range(app.im1.width):
        for y in range(app.im1.height):
            app.pixelData[(x, y)] = False

def defaultMouse(app):
    # default mouseX, mouseY values
    app.cx = 200
    app.cy = 200
    app.dragX = 0
    app.dragY = 0

def imageList(app):
    # images from pinterest
    app.imageList = ['im1', 'im2', 'im3', 'im4', 'im5', 'im6']


    app.im1 = Image.open(f'images/{app.imObj.imList[app.imObj.imIndex]}.png')
    app.imRef = app.im1.load()
    app.image1 = CMUImage(app.im1)

    app.im2 = Image.open('images/canvas.png')
    app.canvas = app.im2.load()
    app.image2 = CMUImage(app.im2)

def currMode(app):
    if app.currDrawing == True:
        app.mode = "Brush"
    elif app.currErasing == True:
        app.mode = "Eraser"
    elif app.currFillMode == True:
        app.mode = "Bucket"

def onAppStart(app):

    app.libImDict = {}
    app.viewingThumb = False

    

    initFileSys(app)
    # print(app.allFiles) #app.allFiles is a list of all files
    drawSubmissions(app)

    app.photo = cv.VideoCapture(0)
    ret, app.frame = app.photo.read()

    
    app.stepsPerSecond = 2

    app.imList = ['im1', 'im2', 'im3', 'im4', 'im5', 'im6']
    # Brush ( brushSize, brushIndex )
    
    app.brushObj = Brush(60, 2) #change the brush index here
    app.imObj = ImageClass(app.imList, 0)
    app.mode = "Brush"
    app.currDrawing = True
    app.currErasing = False
    app.currFillMode = False
    # app.stepsPerSecond = 20 #onstep if needed

    imageList(app)
    app.imObj.referenceImageLoad() # seems that these are broken. 
    app.imObj.canvasImageLoad() # seems that these are broken. 
    app.imObj.libraryImageLoad(app)
    
    
    defaultMouse(app)
    initializeDict(app)
    setBrushSize(app)
    app.bucketObj = Bucket(app.imRef, app.canvas, app.cx, app.cy)

    app.imRef = app.im1.load()
    app.canvas = app.im2.load()

def setBrushSize(app):
    app.brushSize = 20

def onMouseMove(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY
    app.dragX = mouseX
    app.dragY = mouseY



#######################################    THUMBNAILS    ##########################################
    
    

    #for thumbnails
    if 2300 < mouseX < (2300 + 60) and 50 < mouseY < (50 + 80):
        app.viewingThumb = True
        #load image of the thumbnail onto canvas
        print('yes')
        app.imObj.thumbnailImageLoad(0)
        # print(app.thumbnail)
        print(f'{app.reversedAllFiles} lmfao ')
    else:
        app.viewingThumb = False

    if 2300 < mouseX < (2300 + 60) and 50 + 100 < mouseY < (50 + 80 + 100):
        app.viewingThumb = True
        #load image of the thumbnail onto canvas
        print('yes')
        app.imObj.thumbnailImageLoad(1)
    else:
        app.viewingThumb = False

    
    # if 1420 < mouseX < (1420 + 60) and (20 + 80 + 100) < mouseY < (20 + 80 + 100 + 100):
    #     app.viewingThumb = True
    #     #load image of the thumbnail onto canvas
    #     print('yes')
    #     app.imObj.thumbnailImageLoad(app.reversedAllFiles[2])
    #     # print(app.thumbnail)
    # else:
    #     app.viewingThumb = False






#######################################    THUMBNAILS    ##########################################

def isInCanvas(app, mx, my):
    width, height = app.im1.width, app.im1.height
    # returns True if both x and y are within bounds
    return 0 <= mx < width and 0 <= my < height

def onMousePress(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY
    app.dragX = mouseX
    app.dragY = mouseY
    app.bucketObj.mx = app.cx 
    app.bucketObj.my = app.cy
    if app.mode == 'Bucket':
        app.bucketObj.floodFill(app.canvas)
    app.image2 = CMUImage(app.im2)





def onMouseDrag(app, mouseX, mouseY):
    app.imRef = app.im1.load()
    
    app.cx = mouseX 
    app.cy = mouseY 
    app.dragX = mouseX
    app.dragY = mouseY

    if app.currDrawing == True and app.currErasing == False:
        app.brushObj.draw(app, app.imRef, app.canvas, app.cx, app.cy)

    elif app.currErasing == True and app.currDrawing == False:
        app.brushObj.erase(app, app.canvas, app.cx, app.cy)

    # Convert images to CMUImage type
    app.image1 = CMUImage(app.im1)
    app.image2 = CMUImage(app.im2)
  
def onMouseRelease(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    
    # decrease brush size
    if key == 'a':
        app.brushObj.minusBrush()
    
    # increase brush size
    if key == 's':
        app.brushObj.plusBrush()

    # change to eraser mode
    if key == 'e':
        app.currDrawing = False
        app.currErasing = True
        app.currFillMode = False
        app.mode = 'Eraser'
    
    # change to brush mode
    if key == 'b':
        app.currDrawing = True
        app.currErasing = False
        app.currFillMode = False
        app.mode = 'Brush'
        
    if key == 'f':
        app.currDrawing = False
        app.currErasing = False
        app.currFillMode = True
        app.mode = 'Bucket'
    # change reference image    
    if key == 'r':
        app.imObj.changeImageIndex()
        app.imObj.referenceImageLoad()

    # erase whole canvas
    if key == 'y':
        app.imObj.canvasImageLoad()

    # loop through brush type
    if key == 'p':
        app.brushObj.nextBrushIndex()

    # save image feature with unique nameing convention
    if key == '6':
        app.imObj.saveImage(app)
        app.imObj.libraryImageLoad(app)
        app.imObj.libraryImageAdd(app.curFileName)
        # print(f'this is dictionary{app.libImDict}')
        fileSysAppend(app, app.curFileName)
        # print(f'list item you are appending{app.allFiles}')
        
        drawSubmissions(app)

        
        

def redrawAll(app):
    
    # images
    drawImage(app.image1,100,20 + 30)
    drawImage(app.image2, 650+150, 20 + 30)

    if app.viewingThumb is not False:
        drawImage(app.thumbnail, 650 + 150 + 900,20 + 30) #this is supposed to be the canvas2 POS

    # thumbnails
    for i in range(7):
        # print(app.reversedAllFiles[i])
        drawImage(app.libImDict[app.reversedAllFiles[i]], 2300, 20 +30 + (i * 100))
    # drawRect(1420, 20, 60, 80, fill = 'red')
    

    # the mouse cursors
    ### –––––––––––––––––––––––––––––––––––––––––––––––––––––––– ###

    if app.brushObj.brushList[app.brushObj.brushIndex] == 'square':
        drawRect(app.cx, app.cy, app.brushObj.brushSize * 2, app.brushObj.brushSize * 2, fill= None, border = "black", borderWidth = 4, align = 'center')
        drawRect(app.cx - (524+26) - 150 , app.cy, app.brushObj.brushSize * 2, app.brushObj.brushSize * 2, fill= None, border = "red" , borderWidth = 4, align = 'center')
    
    # when drawing circles
    elif app.brushObj.brushList[app.brushObj.brushIndex] == 'circle':
        drawCircle(app.cx, app.cy, app.brushObj.brushSize * 1, fill= None, border = "black", borderWidth = 4)
        drawCircle(app.cx - (524+26) - 150 , app.cy, app.brushObj.brushSize * 1, fill= None, border = "red" , borderWidth = 4)
    
    # when drawing diamond
    elif app.brushObj.brushList[app.brushObj.brushIndex] == 'diamond':
        drawRect(app.cx, app.cy, app.brushObj.brushSize * 1.5, app.brushObj.brushSize * 1.5, fill= None, border = "black", borderWidth = 4, align = 'center' ,rotateAngle = 45)
        drawRect(app.cx - (524+26) - 150 , app.cy, app.brushObj.brushSize * 1.5, app.brushObj.brushSize * 1.5, fill= None, border = "red" , borderWidth = 4, align = 'center', rotateAngle = 45)
    
    ### –––––––––––––––––––––––––––––––––––––––––––––––––––––––– ###
    # debugging labels
    drawLabel(f'dragX: {app.dragX}', 40,100, size= 10)
    drawLabel(f'dragY: {app.dragY}', 40,200, size= 10)

    # drawLabel('press r to change image ', 140,600, size= 20, fill = 'red' ,bold = True)

    drawLabel('A = decrease brush', 650,700, size= 20, bold=True, fill = 'red')
    drawLabel('S = increase brush', 650, 750, size= 20, bold = True, fill = 'red')

    drawLabel('B = brush mode', 140,700, size= 20, bold = True, fill = 'red')
    drawLabel('E = eraser mode', 140, 750, size= 20, bold = True, fill = 'red')

    drawLabel('Y = reset canvas', 850, 700, size = 20, bold= True, fill='red')
    drawLabel('6 = save painting', 850, 750, size = 20, bold= True, fill='red')

    drawLabel('P = brush change', 1380, 750, size = 20, bold= True, fill='red')

    # drawing mode label
    drawLabel(f'MODE: {app.mode}', 750, 30, size = 50, align = 'center', fill = 'red')

def onStep(app):
    app.photo = cv.VideoCapture(0)
    ret, app.frame = app.photo.read()
    app.imObj.referenceImageLoad()
    
    currMode(app)

def main():

    runApp(width=2560, height=1440)

if __name__ == '__main__':
    main()