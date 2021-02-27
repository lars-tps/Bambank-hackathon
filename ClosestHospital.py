
cords = [(1,3),(2,5),(3,6),(7,3)]
hospital = [(2,5) , (6,2)]
# Gives which hospital to go to (hospital 1 or hospital 2)
def calculate(cords,hospital):
    # List of Coordinates, List of Hospital Coordinates
    lst = []
    outerLst = []
    distance = 0
    for i in range (len(cords)):
        lst = []
        for j in range(len(hospital)):
            distance = calcDistance(cords[i][0],cords[i][1],hospital[j][0],hospital[j][1])
            
            lst.append(distance)
        outerLst.append(lst)
    
    bestDistance = []
    for i in range(len(outerLst)):
        temp = calcBestDist(outerLst[i])
        bestDistance.append(temp + 1)
    return bestDistance

def calcDistance(x1,y1,x2,y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

def calcBestDist(lst):
    # Lst of distance
    minVal = lst[0]
    minIndex = 0
    for i in range (len(lst)):
        if i < minVal:
            minVal = lst[i]
            minIndex = i
    return minIndex
