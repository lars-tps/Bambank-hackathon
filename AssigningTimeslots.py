data = open("data.csv")

lst = []
for line in data:
    innerList = []
    line = line.strip()
    line = line.split(',')
    for i in line:
        innerList.append(i)
    lst.append(innerList)
import Priority as pr
print(pr.priority_sort(lst))

data.close()
