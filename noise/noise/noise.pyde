def setup():
    size(500, 500)
    pixelDensity(1)
    noiseDetail(40)
    
xoff = 0
yoff = 10000
start = 0
inc = 0.01
def draw():
    background(0)
    global xoff, yoff
    # To add cloudy effect
    xoff = 0
    loadPixels()
    for x in range(0, width, 1):
        yoff = 0
        for y in range(0, height, 1):
            index = (x + y * width)
            r = noise(xoff, yoff) * 255
            if random(1) > 0:
                pixels[index] = color(r)
            yoff += 0.02
        xoff += 0.02
    updatePixels()
    noLoop()
    
    # Wooden texture 
    # xoff = 0
    # loadPixels()
    # for x in range(0, width, 1):
    #     yoff = 0
    #     for y in range(0, height, 1):
    #         index = (x + y * width)
    #         r = noise(xoff) * 255
    #         if random(1) > 0:
    #             pixels[index] = color(r)
    #         yoff += 0.02
    #     xoff += 0.02
    # updatePixels()
    # noLoop()
    
    
