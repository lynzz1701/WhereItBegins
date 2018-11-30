from random import *
from copy import*

def main():
    global array
    array = rand_array()
    score = 0
    score_ll = [score]
    
    for i in range(4):
        print array[i]
    print "score:",score
        
    global track
    track = [deepcopy(array)]
            
    while True:
        dirct = input("Enter dirct:")
        if dirct != -1:
            score += move(dirct)
            score_ll.append(score)
        elif dirct == -1 and len(track)>0:
            array = track[-2]
            score = score_ll[-2]
            track.pop()
            score_ll.pop()
        for i in range(4):
            print array[i]
        print "score:",score
        


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
    
    if compare(track[-1],array) == False:
        rand_new()
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
