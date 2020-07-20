import math
polygon = list()

# Custom function to return a random number fitting a Gaussian distribution.
def random_gauss(m, sd):
    value = 1
    while value >= 1:
        x1 = random(2) - 1
        x2 = random(2) - 1
        value = x1 * x1 + x2 * x2
    value = math.sqrt(-2 * math.log(value) / value)
    y1 = x1 * value
    y2 = x2 * value
    mean = m or 0
    standardDeviation = sd or 1
    return y1 * standardDeviation + mean

def setup():
    def getCenterPoint(previous, current, standardDeviation):
        # print(previous, current)
        sideX = random_gauss(previous["sideX"] + (current["sideX"] - previous["sideX"]) / 2, standardDeviation)
        sideY = random_gauss(previous["sideY"] + (current["sideY"] - previous["sideY"]) / 2, standardDeviation)
        return { "sideX": sideX, "sideY": sideY }
                                           
    def getMid(mean, standardDeviation):
        newVector = [mean[0]]
        for i in range(1, len(mean), 1):
            previousValue = mean[i - 1]
            currentValue = mean[i]
            midPoint = getCenterPoint(previousValue, currentValue, standardDeviation)
            newVector.append(previousValue)
            print("Previous", previousValue)
            newVector.append(midPoint)
            print("New", midPoint)
        newVector.append(mean[len(mean) - 1])
        return newVector



    global polygon
    size(800, 800)
    background(255)
    colorMode(HSB, 360, 200, 150, 1)
    # Creating a polygon 
    sideAngle = 0.5
    while sideAngle < 6:
        sideX = sin(sideAngle) * width / 4
        sideY = cos(sideAngle) * width / 4
        polygon.append({"sideX": sideX, "sideY": sideY})
        # print(polygon)
        sideAngle += 0.6
    # Midpoint using Gaussian Distribution 
    mid = 50
    while mid > 5:
        for i in range(3):
            polygon = getMid(polygon, mid)
        mid /= 2
    
    
    
def draw():
    global polygon, randomGauss
    for i in range(20):
        push()
        noStroke()
        fill(200, 100, 80, 0.02)
        beginShape()
        translate(width * 0.5, height * 0.5);
        for j in range(len(polygon)):
            currentVector = polygon[j]
            x = random_gauss(currentVector['sideX'], random(25))
            y = random_gauss(currentVector['sideY'], random(25))
            vertex(x, y)
        endShape(CLOSE)
        pop()
    noLoop()
    
