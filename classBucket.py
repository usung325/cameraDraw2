from cmu_graphics import *
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
        startingPix = self.imRef[x, y] #this is the problem
        print('this is running2')
        newColor = self.imRef[x+10, y+10]

        # actually run the helper
        self.dfs(app,self.imRef, self.mx, self.my, newColor, startingPix, canvas,(self.mx - 650),(self.my - 20),0 )
        
        # depth for search method
    def dfs(self, app, imRef, mx, my, newColor, startingPix, canvas, lx, ly, counter):
        counter += 1
        print(f'CLASS XY:{self.mx, self.my}')
        print(f'LOCAL XY:{lx, ly}')
        arbitraryNum = 770
        arbitraryNum2 = 650 + 524

        if mx < 650 or mx > arbitraryNum2 or my < 20 or my > arbitraryNum or imRef[lx, ly] == newColor or imRef[lx , ly] != startingPix or counter == 10:
            print('this is done')
            return
            
        else:
            print('this is recursing')
            # canvas[mx, my] = newColor
            self.helperDfs(self, imRef, canvas, lx, ly)
            self.dfs(self,imRef, mx+1, my, newColor, startingPix, canvas, lx, ly, counter)
            self.dfs(self,imRef, mx-1, my, newColor, startingPix, canvas, lx, ly, counter)
            self.dfs(self,imRef, mx, my+1, newColor, startingPix, canvas, lx, ly, counter)
            self.dfs(self,imRef, mx, my-1, newColor, startingPix, canvas, lx, ly, counter)

    def helperDfs(app, self, imRef, canvas, lx, ly):
        pixelValue = imRef[lx,ly]
        newPixel = tuple(value for value in pixelValue)
        canvas[lx,ly] = newPixel

        app.image2 = CMUImage(canvas)
