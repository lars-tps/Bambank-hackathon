import Priority as pr
data = open("data.csv")
import Priority as pr
lst = []
for line in data:
    innerList = []
    line = line.strip()
    line = line.split(',')
    for i in line:
        if i.isnumeric():
            innerList.append(int(i))
        elif i == "Healthy":
            innerList.append(0)
        elif i == "Infected":
            innerList.append(1)
        elif i == "Singaporean Citizen":
            innerList.append(1)
        elif i == "Foreigner":
            innerList.append(0)
        else:
            innerList.append(i)
    lst.append(innerList)
print(pr.priority_sort(lst))


data.close()
