# 2048
from random import*
from graphics import*
from button import*
import math

class bric:## review
    def __init__(self,wVal,xVal,yVal,value):
        self.w = wVal
        self.x = xVal
        self.y = yVal
        self.v = value
        mycolor = []
        for i in range(10): 
            mycolor.append(color_rgb(250,250-i*15,0))
        self.t = Text(Point(xVal,yVal),"")
        self.t.setSize(30)
        self.t.setTextColor(mycolor[int(math.log(value,2)-1)]) 
        self.t.setText(value)
        self.t.draw(wVal)
        
    def __iadd__(self,other):
        if self.v == other.v:
            self.v += other.v
        else:pass

    def movebric(self):
        self.t.move(0,-1)

    def getValue(self):
        return self.v

    def clear(self):
        self.t.undraw()
        self = 0

def main():
    win = GraphWin("game2048",500,700)
    win.setCoords(-1,6,4,-1)
    for i in range(5):
        Line(Point(i-0.5,-0.5),Point(i-0.5,3.5)).draw(win)
        Line(Point(-0.5,i-0.5),Point(3.5,i-0.5)).draw(win)

    upButton = Button(win,Point(1,4.5),0.7,0.4,"up")
    leftButton = Button(win,Point(0,5),0.7,0.4,"<")
    rightButton = Button(win,Point(2,5),0.7,0.4,">")
    downButton = Button(win,Point(1,5),0.7,0.4,"down")
    upButton.activate()
    leftButton.activate()
    rightButton.activate()
    downButton.activate()

    qButton = Button(win,Point(3,4),0.7,0.4,"Quit")
    rButton = Button(win,Point(3,4.5),0.7,0.4,"Reset")
    uButton = Button(win,Point(3,5),0.7,0.4,"UnDo")
    qButton.activate()
    rButton.activate()

    Text(Point(1,-0.75),"your score:").draw(win)
    score = 0
    sco = Text(Point(2.5,-0.75),"%d"%score)
    sco.draw(win)

    array = rand_array(win)

    while True:
        q = win.getMouse()
        if qButton.clicked(q):
            break
        if rButton.clicked(q):
            for i in range(4):
                for j in range(4):
                    if array[i][j] != 0:
                        array[i][j].clear()
                        array[i][j] = 0
            array = rand_array(win)
            sco.setText("0")
            score = 0
            uButton.deactivate()
        if upButton.clicked(q):
            score += move(array,0)
            sco.setText(str(score))
        if downButton.clicked(q):
            score += move(array,1)
            sco.setText(str(score))
        if leftButton.clicked(q):
            score += move(array,2)
            sco.setText(str(score))
        if rightButton.clicked(q):
            score += move(array,3)
            sco.setText(str(score))
                        ####what if not useful?

def rand_array(win):
    array = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        array.append(row)
    row = sample(range(4),2)
    col = sample(range(4),2)
    array[row[0]][col[0]] = bric(win,col[0],row[0],choice([2,2,4]))
    array[row[1]][col[1]] = bric(win,col[1],row[1],choice([2,2,4]))
    print array
    return array

def move(array,dirct):
    score = 0
    if dirct == 0:
        for i in range(4): ####threading
                done = []
                for j in range(1,4):
                    for l in range(j,0,-1):
                        if array[l][i] != 0:
                            if array[l-1][i] == 0:
                                array[l][i].movebric()
                                array[l-1][i] = array[l][i]
                                array[l][i] = 0                   
                            else:###### ugly
                                a = array[l][i].getValue()
                                if array[l-1][i] == a and (l-1 not in done) and (l not in done):
                                    b = array[l-1][i].getValue()
                                    b += a
                                    array[l][i].clear()
                                    done.append(l-1)
                                    score += b
                                    #####add new nums!
    if dirct == 1:
        for i in range(4):
                done = []
                for j in range(3,0,-1):
                    for l in range(j):
                        if array[l+1][i] == 0:
                            array[l+1][i] = array[l][i]
                            array[l][i].clear()
                        elif array[l+1][i] == array[l][i] and (l+1 not in done) and (l not in done): 
                            array[l+1][i] += array[l][i]
                            array[l][i].clear()
                            done.append(l+1)
                            score += array[l+1][i].getValue()
    if dirct ==2:
        for i in range(4):
            done = []
            for j in range(1,4):
                for l in range(j,0,-1):
                        if array[i][l-1] == 0:
                            array[i][l-1] = array[i][l]
                            array[i][l].clear()
                        elif array[i][l-1] == array[i][l] and (l-1 not in done) and (l not in done):
                            array[i][l-1] += array[i][l]
                            array[i][l].clear()
                            done.append(l-1)
                            score += array[i][l-1].getValue()

    if dirct ==3:
        for i in range(4):
            done = []
            for j in range(3,0,-1):
                for l in range(j):
                        if array[i][l+1] == 0:
                            array[i][l+1] = array[i][l]
                            array[i][l].clear()
                        elif array[i][l+1] == array[i][l] and (l+1 not in done) and (l not in done):
                            array[i][l+1] += array[i][l]
                            array[i][l].clear()
                            done.append(l+1)
                            score += array[i][l+1].getValue()
    return score
    

    
    
                
    
