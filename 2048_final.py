from graphics import*
from button import*
from random import *
from copy import*
import math

class bric:
    def __init__(self,wVal,xVal,yVal,value):
        self.w = wVal
        self.x = xVal
        self.y = yVal
        self.v = value
        mycolor = ["cornsilk","wheat","sandybrown","lightsalmon","salmon","orangered","khaki","gold"]
        font1 = ["saddlebrown"]
        font2 = ["ivory"]
        fontcolor = font1*2 + font2*6
        self.t = Text(Point(xVal,yVal),"")
        self.t.setSize(30)
        self.b = Rectangle(Point(xVal-0.45,yVal-0.45),Point(xVal+0.45,yVal+0.45)) 
        if self.v != 0:
            color = int(math.log(value,2)%8-1)
            self.b.setFill(mycolor[color])
            self.b.setOutline(mycolor[color])
            self.t.setTextColor(fontcolor[color]) 
            self.t.setText(value)
            self.b.draw(wVal)
            self.t.draw(wVal)
    def clear(self):
        self.t.undraw()
        self.b.undraw()
        self = 0

def main():
    
    #background
    global win
    win = GraphWin("game2048",500,700)
    win.setCoords(-1,6,4,-1)
    win.setBackground("floralwhite")
    back = Rectangle(Point(-0.5,-0.5),Point(3.5,3.5))
    back.setFill("oldlace")
    back.draw(win)
    for i in range(5):
        line1 = Line(Point(i-0.5,-0.55),Point(i-0.5,3.55))
        line2 = Line(Point(-0.55,i-0.5),Point(3.55,i-0.5))
        line1.setWidth(12)
        line2.setWidth(12)
        line1.setOutline("tan")
        line2.setOutline("tan")
        line1.draw(win)
        line2.draw(win)
        
    #buttons
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
    
    #score
    Text(Point(1,-0.75),"your score:").draw(win)
    score = 0
    score_ll = [score]
    sco = Text(Point(2.5,-0.75),"%d"%score)
    sco.draw(win)

    #not_GUI array
    global array
    array = rand_array()
    
    #GUI_array
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
            
    while check():
        print "track:",len(track)
        if len(track)>1:
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
            for i in range(4):
                for j in range(4):
                    GUI_array[i][j].clear()
                    GUI_array[i][j] = (bric(win,j,i,array[i][j]))
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
            track.pop()
            score_ll.pop()
            array = deepcopy(track[-1])
            score = score_ll[-1]
            sco.setText(str(score))
            for i in range(4):
                for j in range(4):
                    GUI_array[i][j].clear()
                    GUI_array[i][j] = (bric(win,j,i,array[i][j]))
        for i in range(4):
            print array[i]
        print "score:",score
    while not check():
        loser = Text(Point(1.5,1.5),"You Lose...")
        loser.setSize(35)
        loser.draw(win)
        Text(Point(1.5,2),"Press anywhere to quit...").draw(win)
        win.getMouse()
        break
    win.close()
        


def rand_array(): 
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
    if dirct == 0:#up
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
    if dirct == 1:#down
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
    if dirct ==2:#left
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

    if dirct ==3:#right
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
                        
        

    if compare(track[-1],array) == False:# when efficient
        rand_new()
        for i in range(4):
            for j in range(4):
                if array[i][j] != track[-1][i][j]:
                    GUI_array[i][j].clear()
                    GUI_array[i][j] = (bric(win,j,i,array[i][j]))
        step = deepcopy(array)
        track.append(step)

    return score
    

def rand_new():# new num
    row = choice(range(4))
    col = choice(range(4))
    if array[row][col] == 0:
        array[row][col] = choice([2,2,4])
    else: rand_new()

def compare(list1,list2): # whether or not efficirnt
    for i in range(4):
        for j in range(4):
            if list1[i][j] == list2[i][j]:
                pass
            else: return False
    return True

def check():# whether or not go on
    for i in range(4):
        if 0 in array[i]:
            return True
    for i in range(3):
        for j in range(3):
            if array[i][j] == array[i+1][j] or array[i][j] ==array[i][j+1]:
                return True
    for i in range(3):
        if array[3][i] ==array[3][i+1] or array[i][3] == array[i+1][3]:
            return True
    return False


main()
