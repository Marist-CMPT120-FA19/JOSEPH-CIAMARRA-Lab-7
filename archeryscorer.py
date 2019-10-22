from graphics import *
import math


 
def distform(point, circle):
    x = point.getX() - circle.getCenter().getX()
    y = point.getY() - circle.getCenter().getY()
    dist = math.sqrt(x*x + y*y)

    return dist <= circle.getRadius()

    
def main():

    score=0
    
    win = GraphWin('Archery',300,300)
    center=Point(150, 150)

    white=Circle(center,100)
    white.setFill("white")
    white.draw(win)

    black=Circle(center,80)
    black.setFill("black")
    black.draw(win)

    blue=Circle(center, 60)
    blue.setFill("blue")
    blue.draw(win)

    red=Circle(center, 40)
    red.setFill("red")
    red.draw(win)

    yellow=Circle(center,20)
    yellow.setFill("yellow")
    yellow.draw(win)

    for x in range(5):
        click= win.getMouse()
        
        if(distform(click, yellow)):
            score += 9
            print("+9")
        elif(distform(click, red)):
            score += 7
            print("+7")
        elif(distform(click, blue)):
            score += 5
            print("+5")
        elif(distform(click, black)):
            score += 3
            print("+3")
        elif(distform(click, white)):
            score += 1
            print("+1")
        else:
            score += 0
            print("+0")
    
    
    print("Total Points: ", score)

                    
    win.getMouse()
    win.close()
    
main()
