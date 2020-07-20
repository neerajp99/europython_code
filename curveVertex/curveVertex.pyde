def setup():
    size(700, 700)
    background("#013840");


def draw():
    for i in range(40, width - 30, 40): 
        for j in range(40, height - 30, 40):
            strokeWeight(1.3);
            stroke(255);
            noFill();
            beginShape();
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            curveVertex(i + random(-10, 10), j + random(-10, 10));
            endShape();
    noLoop();
