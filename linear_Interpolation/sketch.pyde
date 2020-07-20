def setup():
    size(600, 600)
    background(255)
    colorMode(HSB, 360, 100, 100);

# def keyPressed(e):
#     if e.key.lower() == 's':
#         save('img_11.jpg');
    
def draw():
    initialColor = color(0,50,100);
    finalColor = color(45, 80, 100);
    noStroke()
    for i in range(width):
        linearIntValue = map(i, 0, width, 0, 1.0)
        # Calculates a color between two colors at a specific increment. 
        linearIntColor = lerpColor(initialColor, finalColor, linearIntValue)
        fill(linearIntColor)
        rect(i, 0, 25, height)
    noLoop()
