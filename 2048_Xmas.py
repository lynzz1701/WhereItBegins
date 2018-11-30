from graphics import*
from button import*
from random import *
from copy import*
import math

class bric:## review
    def __init__(self,wVal,xVal,yVal,value):
        self.w = wVal
        self.x = xVal
        self.y = yVal
        self.v = value
        mycolor = []
        for i in range(10): 
            mycolor.append(color_rgb(250,250-i*15,0)) #limit my num
        self.t = Text(Point(xVal,yVal),"")
        self.t.setSize(30)
        if self.v != 0:
            self.t.setTextColor(mycolor[int(math.log(value,2)-1)]) 
            self.t.setText(value)
        self.t.draw(wVal)

    def clear(self):
        self.t.undraw()
        self = 0

def main():
    global win
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
    score_ll = [score]
    sco = Text(Point(2.5,-0.75),"%d"%score)
    sco.draw(win)

    global array
    array = rand_array()

    global GUI_array
    GUI_array = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(bric(win,j,i,array[i][j]))
        GUI_array.append(row)
  
    for i in range(4):
        print array[i]
    print "score:",score
        
    global track
    track = [deepcopy(array)]
            
    while True:
        print len(track)
        if len(track)>1:#####
            uButton.activate()
        else:
            uButton.deactivate()
        q = win.getMouse()
        if qButton.clicked(q):
            break
        if rButton.clicked(q):
            array = rand_array()
            track = [deepcopy(array)]
            sco.setText("0")
            score = 0
            score_ll = [score]
        if upButton.clicked(q):
            score += move(0)
            sco.setText(str(score))
            score_ll.append(score)
        if downButton.clicked(q):
            score += move(1)
            sco.setText(str(score))
            score_ll.append(score)
        if leftButton.clicked(q):
            score += move(2)
            sco.setText(str(score))
            score_ll.append(score)
        if rightButton.clicked(q):
            score += move(3)
            sco.setText(str(score))
            score_ll.append(score)
        if uButton.clicked(q) and len(track)>1:
            array = track[-2]###
            score = score_ll[-2]###
            sco.setText(str(score))
            track.pop()####
            score_ll.pop()
            if len(track)>1:
                track.pop()
                score_ll.pop()
            for i in range(4):
                for j in range(4):
                    GUI_array[i][j].clear()
                    GUI_array[i][j] = (bric(win,j,i,array[i][j]))
        for i in range(4):
            print array[i]
        print "score:",score
    win.close()
        


def rand_array(): # initial
    array = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        array.append(row)
    row = sample(range(4),2)
    col = sample(range(4),2)
    array[row[0]][col[0]] = choice([2,2,4])
    array[row[1]][col[1]] = choice([2,2,4])
    return array

def move(dirct):
    score = 0
    if dirct == 0:
        for i in range(4):
                done = []
                for j in range(1,4):
                    for l in range(j,0,-1):
                        if array[l-1][i] == 0:
                            array[l-1][i] = array[l][i]
                            array[l][i] = 0
                        elif array[l-1][i] == array[l][i] and (l-1 not in done) and (l not in done):
                            array[l-1][i] += array[l][i]
                            array[l][i] = 0
                            done.append(l-1)
                            score += array[l-1][i]
    if dirct == 1:
        for i in range(4):
                done = []
                for j in range(3,0,-1):
                    for l in range(j):
                        if array[l+1][i] == 0:
                            array[l+1][i] = array[l][i]
                            array[l][i] = 0
                        elif array[l+1][i] == array[l][i] and (l+1 not in done) and (l not in done): 
                            array[l+1][i] += array[l][i]
                            array[l][i] = 0
                            done.append(l+1)
                            score += array[l+1][i]
    if dirct ==2:
        for i in range(4):
            done = []
            for j in range(1,4):
                for l in range(j,0,-1):
                        if array[i][l-1] == 0:
                            array[i][l-1] = array[i][l]
                            array[i][l] = 0
                        elif array[i][l-1] == array[i][l] and (l-1 not in done) and (l not in done):
                            array[i][l-1] += array[i][l]
                            array[i][l] = 0
                            done.append(l-1)
                            score += array[i][l-1]

    if dirct ==3:
        for i in range(4):
            done = []
            for j in range(3,0,-1):
                for l in range(j):
                        if array[i][l+1] == 0:
                            array[i][l+1] = array[i][l]
                            array[i][l] = 0
                        elif array[i][l+1] == array[i][l] and (l+1 not in done) and (l not in done):
                            array[i][l+1] += array[i][l]
                            array[i][l] = 0
                            done.append(l+1)
                            score += array[i][l+1]
                        
        

    if compare(track[-1],array) == False:#####
        rand_new()
        for i in range(4):
            for j in range(4):
                GUI_array[i][j].clear()
                GUI_array[i][j] = (bric(win,j,i,array[i][j]))
        step = deepcopy(array)
        track.append(step)

    return score
    

def rand_new():
    row = choice(range(4))
    col = choice(range(4))
    if array[row][col] == 0:
        array[row][col] = choice([2,2,4])
    else: rand_new()

def compare(list1,list2):
    for i in range(4):
        for j in range(4):
            if list1[i][j] == list2[i][j]:
                pass
            else: return False
    return True

main()
