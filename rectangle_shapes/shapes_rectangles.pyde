def setup():
    i = 0
    size(500, 700)
    background(0)
    
 
def drawNoise(x, y, size):
    push()
    translate(x, y)
    
    for i in range(0, 500, 1):
        x = random(0, size)
        y = random(0, size)
        w = random(1, 3)
        h = random(1, 3)
        noStroke()
        fill(random(250))
        if random(0, 1) > 0.7:
            ellipse(x, y, w, h)
    print('hello')
    pop() 
    
def draw():
    for y in range(0, 700, 10):
        x1 = random(0, 500)
        x2 = 500 - x1
        print(x1, x2)
        
        noStroke()
        fill(random(255))
        rect(0, y, int(x1), 15)
        fill(random(255))
        rect(int(x1), y, 500, 15)
        # for i in range(0, int(x1), 40):
        #     push()
        #     fill(random(255))
        #     rect(i, y, 40, 15)
        #     pop()
        # for j in range(int(x1), 500, 40):
        #     push()
        #     fill(random(255))
        #     rect(j, y, 40, 15) 
        #     pop()
        # drawNoise(0,0,700)
        
    noLoop()
