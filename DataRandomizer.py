import random

def randomize(x):
    #Main Code
    # ID, Age, Cords
    data = open("data.csv",'w')
    data.writelines("ID, Age,Infection Status,CoordinatesResidency Status\n")
    ID = randomizeID(x)
    age = randomizeAge(x)
    status = randomizeInfectionStatus(x)
    cords = randomizeCords(x)
    residence = randomizeResidence(x)
    for j in range(len(ID)):
        data.writelines(ID[j] + "," + age[j] + "," + status[j] + "," +str(cords[j])+","+residence[j]+ "\n")
    data.close()
    
def randomizeAge(upper_bounds):
    lst = []
    for i in range(upper_bounds):
        j = random.randint(1,100)
        lst.append(str(j))
    return lst
    
def randomizeID(upper_bounds):
    res = []
    for i in range(1,upper_bounds+1):
        res.append(str(i))
    return res
       
def randomizeCords(upper_bounds):
    lst = []
    for i in range(upper_bounds):
        x = random.randrange(1296798,1423013)
        y = random.randrange(103910251,103914775)
        coords = x,y
        lst.append(coords)
    return lst

def randomizeInfectionStatus(upper_bound):
    lst = []
    ans = []
    for i in range(upper_bound):
        lst.append(random.randint(0,1))
    for i in lst:
        if i:
            ans.append("Infected")
        else:
            ans.append("Healthy")
    return ans

def randomizeResidence(upper_bounds):
    lst = []
    ans = []
    for i in range (upper_bounds):
        lst.append(random.randint(0,1))
    for i in lst:
        if i:
            ans.append("Singaporean Citizen")
        else:
            ans.append("Foreigner")
    return ans

randomize(999)
