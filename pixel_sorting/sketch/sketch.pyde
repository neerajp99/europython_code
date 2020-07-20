from functools import reduce
def setup():
    global img, imgNew
    size(700, 400)
    background(0)
    img = loadImage("sketch.jpg")
    imgNew = loadImage("sketch.jpg")
    imgNew.resize(700, 500)
    img.resize(700,400)
    # imageMode(CENTER);
    img.loadPixels()
    colorMode(RGB)    
    
def convert_to_rgb(hexcode):
    hexcode = hexcode.lstrip('-')
    return list(int(hexcode[i:i+2], 16) for i in (0, 2, 4))
    
def draw():
    global img, imgNew
    image(img, 0, 0)
    pixelArray = img.pixels
    # Looping through rows and columns 
    for x in range(img.height):
        newPixelArray = list()
        for y in range(img.width):
            # Get pixel positions 
            pixel = img.get(y, x)
            if len(str(pixel)) < 6:
                pixel = -9757152
            # Get the pixel hex value and convert it into rgb
            rgbPixel = convert_to_rgb(str(pixel))
            rgbPixel.append(255)
            newPixelArray.append(rgbPixel)
            # print(type(pixel))
    
        # Sort the new pixel array 
        for j in range(len(newPixelArray) - 2):
            # for j in range (len(newPixelArray) - 2):
            if ((((newPixelArray[j][0] + newPixelArray[j][1] + newPixelArray[j][2])) > (newPixelArray[j+1][0] + newPixelArray[j+1][1] + newPixelArray[j+1][2]))):
                newPixelArray[j], newPixelArray[j+1] = newPixelArray[j+1], newPixelArray[j]
                
        # Set the image pixels to the second image
        for i in range(img.width):
            a = newPixelArray[i][0]
            b = newPixelArray[i][1]
            c = newPixelArray[i][2]
            cl = color(a, b, c)
            imgNew.set(i, x, cl)
    print('jajaja')     
    imgNew.updatePixels();
    image(imgNew,0,0);
    noLoop()


    
