def setup():
    global points
    size(700, 700)
    background(255)
    points = []
    # Loop over and create random x, y vectors 
    for i in range(2000):
        newVector = PVector(random(width + 100), random(height))
        # Push the newly created vector points to the points array
        points.append(newVector)
    
def draw():
    global points
    for i in range(len(points)):
        noFill()
        noiseSeed(2)
        vectorObject = points[i]
        stroke("#333");
        strokeWeight(0.3);
        beginShape()
        for i in range(20):
            # Generate noise values and map it between 0 and 2*PI radians
            noiseValue = map(noise(vectorObject.x / 500, vectorObject.y / 500), 0, 1, 0, 2*PI)
            x1 = vectorObject.x
            y1 = vectorObject.y 
            x2 = x1 + cos(noiseValue)
            y2 = y1 + sin(noiseValue)
            vertex(x1, y1)
            vectorObject.x = x2 
            vectorObject.y = y2
        endShape(OPEN)
