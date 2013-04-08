from SimpleCV import *

def colorDistance(color1,color2):
    return ((color2[0]-color1[0])**2+(color2[1]-color1[1])**2+(color2[2]-color1[2])**2)

def findWorkspace():
    count = 0
    while (1):
        i = cam.getImage()
        layer = DrawingLayer(i.size())
        i.addDrawingLayer(layer)
        inverted = i.hueDistance(color=Color.WHITE,minsaturation=75,minvalue=100).binarize()
        blobs = inverted.findBlobs()
        squares = []
        if blobs:
            for blob in blobs:
                if blob.isSquare(.2,.2):
                    area = blob.minRectWidth()*blob.minRectHeight()
                    if area>1000:
                        squares.append(blob)
                        blob.draw(color=Color.GREEN,width=-1,layer=layer)
        i.show()

        # wait until we see 4 squares for 3 frames in a row
        if len(squares) == 4:
            count += 1
            if count >= 3:
                break
        else:
            count = 0

    #get the center of the squares (to determine upper left, etc)
    center = [0,0]
    for square in squares:
        center[0] += square.minRectX()
        center[1] += square.minRectY()
    center[0] /= 4
    center[1] /= 4

    #find bounds of workspace (the rectangle defined by the squares' inside corners)
    workspace = []
    left = -9999
    right = 9999
    top = -9999
    bottom = 9999

    #NOTE: coordinate system origin is in upper left corner
    for square in squares:
        x = square.minRectX()
        y = square.minRectY()
        w = square.minRectWidth()
        h = square.minRectHeight()
        if x < center[0] and y > center[1]: #lower left square
            i.drawCircle((x,y),4,color=Color.RED,thickness=-1)
            if x+w/2. > left:
                left = x+w/2.
            if y-h/2. < bottom:
                bottom = y-h/2.
            workspace.append([x+w/2.,y-h/2.])
        if x > center[0] and y > center[1]: #lower right square
            i.drawCircle((x,y),4,color=Color.BLUE,thickness=-1)
            if x-w/2. < right:
                right = x-w/2.
            if y-h/2. < bottom:
                bottom = y-h/2.
            workspace.append([x-w/2.,y-h/2.])
        if x < center[0] and y < center[1]: #upper left square
            i.drawCircle((x,y),4,color=Color.YELLOW,thickness=-1)
            if x+w/2. > left:
                left = x+w/2.
            if y+h/2. > top:
                top = y+h/2.
            workspace.append([x+w/2.,y+h/2.])
        if x > center[0] and y < center[1]: #upper right square
            i.drawCircle((x,y),4,color=Color.WHITE,thickness=-1)
            if x-w/2. < right:
                right = x-w/2.
            if y+h/2. > top:
                top = y+h/2.
            workspace.append([x-w/2.,y+h/2.])

    w = (right-left)
    h = (bottom-top)
    i.drawRectangle(left,top,w,h,alpha=45,width=-1,color=Color.BLACK)

    '''while 1:
        i.show()''' #uncomment to see inner process of findWorkspace()

    return [left,top,w,h]

cam = Camera(1)
ws = findWorkspace() #workspace
while (1):
    i = cam.getImage()
    i = i.crop(ws[0],ws[1],ws[2],ws[3]) #only use the workspace
    layer = DrawingLayer(i.size())
    i.addDrawingLayer(layer)
    lines = i.binarize().findLines(cannyth1=10,cannyth2=150)
    print lines
    if lines:
        for line in lines:
            #line.draw(layer=layer)
            i.drawLine(line.points[0],line.points[1])

    i.show()


