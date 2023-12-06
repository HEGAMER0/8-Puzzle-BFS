
def moveUp(move=[]):
    for i in range(3):
        for j in range(3):
            if move[i][j]==0:
                locZ=[i,j]
    if locZ[0]-1!=-1:
        move[locZ[0]][locZ[1]],move[locZ[0]-1][locZ[1]]=move[locZ[0]-1][locZ[1]],move[locZ[0]][locZ[1]]
        
        return move
def moveRight(move=[]):
    for i in range(3):
        for j in range(3):
            if move[i][j]==0:
                locZ=[i,j]
    if locZ[1]+1!=3:
        move[locZ[0]][locZ[1]],move[locZ[0]][locZ[1]+1]=move[locZ[0]][locZ[1]+1],move[locZ[0]][locZ[1]]
        
        return move

def moveLeft(move=[]):
    for i in range(3):
        for j in range(3):
            if move[i][j]==0:
                locZ=[i,j]
    if locZ[1]-1!=-1:
        move[locZ[0]][locZ[1]],move[locZ[0]][locZ[1]-1]=move[locZ[0]][locZ[1]-1],move[locZ[0]][locZ[1]]
        return move

def moveDown(iState):
    for i in range(3):
        for j in range(3):
            if iState[i][j]==0:
                locZ=[i,j]
    if locZ[0]+1!=3:
        iState[locZ[0]][locZ[1]],iState[locZ[0]+1][locZ[1]]=iState[locZ[0]+1][locZ[1]],iState[locZ[0]][locZ[1]]
        
        return iState



iState=[[1,4,2],[3,0,8],[6,5,7]]
gState=[[0,1,2],[3,4,5],[6,7,8]]
path=[]
queue=[]
queue.append(iState)
def solverBFS(HO):
    hi =[]
    hi =[li[:] for li in HO]
    while queue:
        for moveFun in [moveLeft,moveUp,moveRight,moveDown]:
            newState = [row[:] for row in hi]
            s=moveFun(newState)
            
            queue.append(s)
        m=queue.pop(0)
        if m==gState:
            return m
        elif m!=None:

            hi = m
            
print(solverBFS(iState))           


             

            
        
        
    
    
    
