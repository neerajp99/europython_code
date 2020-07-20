r, g, b = 175, 130, 215
translateX, translateY = 0, 0
opacity = 255
zoff = 0
def setup():
    size(800, 800)
    background(0)
    frameRate(30)
    global rad
    rad = 2

def draw():
    global rad, r, g, b, translateX, translateY, opacity, zoff
    noFill()
    stroke(r, g, b, opacity)
    beginShape()
    a = 0
    while a < TWO_PI:
        xoff = map(cos(a), -1, 1, 0, 10)
        yoff = map(sin(a), -1, 1, 0, 10)
        noiseFactor = map(noise(xoff, yoff, zoff), 0, 1, 100, 150)
        x = width / 2 + rad *  noiseFactor * cos(a)
        y = height / 2 + rad *  noiseFactor * sin(a)
        curveVertex(x, y)
        a += 0.1
    endShape(CLOSE)
    zoff += 0.1
    rad -= 0.02
    # if frameCount > 50:
    #     translateX, translateY = 0, 0
    if r > 255:
        r = 0
    if g > 255:
        g = 0
    if b > 255:
        b = 0
    if opacity == 0:
        opacity = 255
    opacity -= 1
    r += 1
    g += 1
    b += 1
    
    
