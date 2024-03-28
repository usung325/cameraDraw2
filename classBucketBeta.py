from cmu_graphics import *
from classBeta import * # All Classes
from PIL import Image, ImageDraw
import os, pathlib
import math
import string
import random

class Bucket():
    def __init__(self, imRef, canvas, mx, my):
        self.imRef = imRef
        self.canvas = canvas
        self.mx = mx
        self.my = my
    
    # Referenced skeleton of: https://www.youtube.com/watch?v=hEZ8uGqaC2c
    def floodFill(self, canvas):
        x,y = ((self.mx - 650), (self.my - 20))
        print('this is running')
        startingPix = self.canvas[x, y] #this is where you are starting
        print('this is running2')
        newColor = self.imRef[x, y] 

        # actually run the helper
        self.dfs(app,self.imRef, self.mx, self.my, newColor, startingPix, canvas,(self.mx - 650),(self.my - 20),0 )
        
        # depth for search method
    def dfs(self, app, imRef, mx, my, newColor, startingPix, canvas, lx, ly, counter):
        counter += 1
        print(f'CLASS XY:{self.mx, self.my}')
        print(f'LOCAL XY:{lx, ly}')
        arbitraryNum = 770
        arbitraryNum2 = 650 + 524

        print(imRef[lx, ly] == startingPix)
        # print(canvas[lx , ly] != newColor)
        #when x == certain value
        #when canvas pixel rgb values does not equal initial canvas pixel rgb value
        if mx < 650 or mx > arbitraryNum2 or my < 20 or my > arbitraryNum or canvas[lx, ly] != startingPix or counter == 1:
            print('this is done')
            return
            
        else:
            print('this is recursing')
            # canvas[mx, my] = newColor
            self.helperDfs(self, imRef, canvas, lx, ly)
            self.dfs(self,imRef, mx, my, newColor, startingPix, canvas, lx+1, ly, counter)
            self.dfs(self,imRef, mx, my, newColor, startingPix, canvas, lx-1, ly, counter)
            self.dfs(self,imRef, mx, my, newColor, startingPix, canvas, lx, ly+1, counter)
            self.dfs(self,imRef, mx, my, newColor, startingPix, canvas, lx, ly-1, counter)

    def helperDfs(self, app, imRef, canvas, lx, ly): #this works. just needs to get base cases working
        # if Brush.isInCanvas(self, app, lx, ly): #check for it's inside the canvas but dont' need this rn
        pixelValue = imRef[lx,ly]
        newPixel = tuple(value for value in pixelValue)
        canvas[lx,ly] = newPixel
                
        app.image1 = CMUImage(imRef)
        app.image2 = CMUImage(canvas)

    
