import random

def randomize(x):
    #Main Code
    # ID, Age, Cords
    data = open("data.csv",'w')
    data.writelines("ID, Age,Infection Status,CoordinatesResidency Status\n")
    ID = randomizeID(InttoList(x))
    age = randomizeAge(x)
    status = randomizeInfectionStatus(x)
    cords = randomizeCords(x)
    residence = randomizeResidence(x)
    for j in range(len(ID)):
        data.writelines(ID[j] + "," + age[j] + "," + status[j] + "," +str(cords[j])+","+residence[j]+ "\n")
    data.close()
    
def InttoList(y):
    # 923 = [9,2,3]
    lst = []
    while y != 0:
        num = y%10
        y //= 10
        lst.append(num)
    lst.reverse()
    return lst
def randomizeAge(upper_bounds):
    lst = []
    for i in range(upper_bounds):
        j = random.randint(1,100)
        lst.append(str(j))
    return lst
    
def randomizeID(upper_bounds):
    def lex_suc(current,bound):
        # [0,1,1] = [1,0,0]
        # [1,0,0] = [1,0,1]
        i = len(current)-1
        while current[i] == bound[i]:
            current[i] = 0
            i -= 1
        current[i] += 1
        return current
    
    first = [0] * len(upper_bounds)
    last = upper_bounds
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1],upper_bounds)[:]]
    res = joinList(res)
    res.pop()
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
def joinList(lst):
    ans = ""
    lstt = []
    for i in range (len(lst)):
        ans = ""
        for j in lst[i]:
            ans += str(j)
        lstt.append(ans)
    return lstt
randomize(999)