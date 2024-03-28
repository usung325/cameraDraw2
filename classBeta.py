from cmu_graphics import *
from PIL import Image, ImageDraw
import cv2 as cv
import os, pathlib
import math
import string
import random
import time

class Brush():
    def __init__(self, brushSize, brushIndex):
        self.brushList = ['square', 'circle', 'diamond']
        self.brushSize = brushSize
        self.brushIndex = brushIndex
        self.brushX = 650+150
        self.brushY = 20 + 30

    def plusBrush(self):
        self.brushSize += 20

    def minusBrush(self):
        if self.brushSize > 20:
            self.brushSize -= 20

    def nextBrushIndex(self):
        if self.brushIndex < 2:
            self.brushIndex += 1
        else:
            self.brushIndex = 0

    def isInCanvas(self, app, n, m):
        width, height = app.im1.width, app.im1.height
        # returns True if both x and y are within bounds
        return 0 <= n < width and 0 <= m < height

    def dist(self, x1,y1,x2,y2):
        dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        return dist
    
    def manhattanDist (self, x1, y1, x2, y2):
        dist = (abs(x1 - x2) + abs(y1-y2))
        return dist

    #the main draw function
    def draw(self, app, imRef, canvas, mx, my):
        if self.brushList[self.brushIndex] == 'square':
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    
                    if Brush.isInCanvas(self, app, n, m):
                        # pixelValue = imRef[n,m]
                        # newPixel = tuple(value for value in pixelValue)

                        
                                                # #––––––––––––––––##–––COLOR EDITTING––––##––––––––––––––––##––––––––––––––––#
                                                # # Convert newPixel to a list to modify color channels
                                                # newPixelList = list(newPixel)
                                                
                                                # # [0] == red [1] == green [2] == blue
                                                # newRed = newPixelList[0] + 150  
                                                # newPixelList[0] = newRed
                                                # newPixel = tuple(newPixelList)
                                                # #––––––––––––––––##––––COLOR EDITING––––##––––––––––––––––##––––––––––––––––#
                        # canvas[n,m] = newPixel
                        canvas[n,m] = imRef[n,m]
                
            app.image1 = CMUImage(imRef)
            app.image2 = CMUImage(canvas)

        elif self.brushList[self.brushIndex] == 'circle':
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    if Brush.isInCanvas(self, app, n, m):
                        if self.dist(x,y,n,m) <= self.brushSize:
                            # pixelValue = imRef[n,m]
                            # newPixel = tuple(value for value in pixelValue)
                            # canvas[n,m] = newPixel
                            print('lol', imRef[n,m])
                            print('wow',canvas[n,m])
                            canvas[n,m] = imRef[n,m]
                
            app.image1 = CMUImage(imRef)
            app.image2 = CMUImage(canvas)



        elif self.brushList[self.brushIndex] == 'diamond': ############################################## JAN 31 ##############################
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    if Brush.isInCanvas(self, app, n, m):
                        if self.manhattanDist(x,y,n,m) <= self.brushSize:
                            # pixelValue = imRef[n,m]

                            # newPixel = tuple(value for value in pixelValue)
                            
                            # canvas[n,m] = newPixel
                                                        # pixelValue = imRef[n,m]
                                                        # newPixel = tuple(value for value in pixelValue)

                                                        
                                                        # #––––––––––––––––##–––COLOR EDITTING––––##––––––––––––––––##––––––––––––––––#
                                                        # # Convert newPixel to a list to modify color channels
                                                        # newPixelList = list(newPixel)
                                                        
                                                        # # [0] == red [1] == green [2] == blue
                                                        # newRed = int(newPixelList[0] * 0.299 + newPixelList[1] * 0.587 + newPixelList[2] * 0.114)

                                                        # newPixelList.pop()
                                                        # newPixelList.pop()
                                                        # newPixelList[0] = newRed
                                                        # print(newPixelList)
                                                        # newPixel = newPixelList[0]
                                                        
                                                        # #––––––––––––––––##––––COLOR EDITING––––##––––––––––––––––##––––––––––––––––#
                                                        # canvas[n,m] = newPixel
                                                        # print(newPixel)

                            ##### standalone #####
                            print(imRef[n,m])
                            canvas[n,m] = imRef[n,m]
                            print(canvas[n,m])
                            
                            ##### standalone #####
                            
                            ############################################## JAN 31 ##############################









            app.image1 = CMUImage(imRef)
            app.image2 = CMUImage(canvas)

    def erase(self, app, canvas, mx,my):
        if self.brushList[self.brushIndex] == 'square':
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    if Brush.isInCanvas(self, app, n, m):
                        canvas[n,m] = 255

            app.image2 = CMUImage(canvas)

        elif self.brushList[self.brushIndex] == 'circle':
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    if Brush.isInCanvas(self, app, n, m):
                        if self.dist(x,y,n,m) <= self.brushSize:
                            canvas[n,m] = 255

            app.image2 = CMUImage(canvas)
        
        elif self.brushList[self.brushIndex] == 'diamond':
            x,y = ((mx - self.brushX), (my - self.brushY))
            for n in range(x-self.brushSize, x + self.brushSize + 1):
                for m in range(y-self.brushSize, y + self.brushSize + 1):
                    if Brush.isInCanvas(self, app, n, m):
                        if self.manhattanDist(x,y,n,m) <= self.brushSize:
                            canvas[n,m] = 255

            app.image2 = CMUImage(canvas)

### ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ###
### –––––––––––––––––––––––––––––CLASS––––––––––––––––––––––––––––––––––––– ###
### ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ###
class ImageClass():
    def __init__(self, imList, imIndex):
        self.imList = imList
        self.imIndex = imIndex
        self.counter = 0
        self.seshIdList = []

    def libraryImageLoad(self, app):

        entireImFiles = [file for file in app.allFiles if file.lower().endswith(('.png'))] #filter only stuff thats png
        app.libImDict.clear()  # Initialize the dictionary outside the loop
        for i, file in enumerate(entireImFiles):
            print(f'{file}lmfaooooooo')  # Print the filename
            image_path = f"submissions/{file}"
            image = Image.open(image_path)
            image = image.convert("L")  # Convert to grayscale
            image = image.convert('1', dither=Image.Dither.FLOYDSTEINBERG)  # Apply dithering
            image= image.resize((60, 80))
            app.libImDict[file] = CMUImage(image)  # Store the processed image
        print(f'this is it{app.libImDict}')

    def libraryImageAdd(self, file):
        image_path = f"submissions/{file}.png"
        image = Image.open(image_path)
        image = image.convert("L")  # Convert to grayscale
        image = image.convert('1', dither=Image.Dither.FLOYDSTEINBERG)  # Apply dithering
        image= image.resize((60, 80))
        app.libImDict[f'{file}.png'] = CMUImage(image)




    def referenceImageLoad(self):
        
        ############################################## JAN 31 ##############################
        
        

        # cv.imwrite('images/captured_frame.png', app.frame)
        # app.photo.release()
        
        # opencv_image=cv.imread(app.frame) # open image using openCV2
        
        color_coverted = cv.cvtColor(app.frame, cv.COLOR_BGR2RGB)
        app.cvToPIL = Image.fromarray(color_coverted)
        app.im1 = app.cvToPIL # this is a test

        app.im1 = app.im1.resize((600 - 55, 800 + 200 - 250), Image.Resampling.LANCZOS)
        # app.im1 = app.im1.crop(20)
        app.im1 = app.im1.transpose(Image.FLIP_LEFT_RIGHT)
        app.im1 = app.im1.convert('1', dither= Image.Dither.FLOYDSTEINBERG) # THIS FUCKS (TRY TURNING ON)

        app.image1 = CMUImage(app.im1)
        

        ################## delete top and uncomment bottom 1_30_2024 ####################

        # app.im1 = Image.open(f'images/{self.imList[self.imIndex]}.png')
        # app.imRef = app.im1.load()
        # app.image1 = CMUImage(app.im1)  

    def canvasImageLoad(self):
        app.im2 = Image.open('images/canvas3.png')

        # app.im2 = app.im2.convert('L', dither = Image.Dither.FLOYDSTEINBERG )
        app.im2 = app.im2.convert("L") # this is working
        app.im2 = app.im2.convert('1', dither= Image.Dither.FLOYDSTEINBERG) 
        # Same thing as above comment line


        app.canvas = app.im2.load()
        app.image2 = CMUImage(app.im2)  # undo this

    def thumbnailImageLoad(self, file):
        print(file)
        image_path = f"submissions/{app.reversedAllFiles[file]}"
        app.thumbnail = Image.open(image_path)
        app.thumbnail = CMUImage(app.thumbnail)



        

        

    def changeImageIndex(self):
        if self.imIndex < len(app.imObj.imList)-1:
            self.imIndex += 1
            app.im1 = Image.open(f'images/{self.imList[self.imIndex]}.png')
        else:
            self.imIndex = 0
            app.im1 = Image.open(f'images/{self.imList[self.imIndex]}.png')

    def saveImage(self, app):
        self.counter += 1
        if self.counter == 1:    
            self.sessionId = self.randFileName()
        self.seshIdList.append(self.sessionId)
        app.curFileName = f"{self.seshIdList[0]}_{self.counter}"
        app.im2.save(f"submissions/{app.curFileName}.png")

        # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    def randFileName (self, size = 4, chars = string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))