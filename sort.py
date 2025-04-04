thislist = [10, 90, 5, 3]

for i in range(len(thislist)):
    for j in range(len(thislist) - 1):
        if thislist[j] > thislist[j+1]:
            t = thislist[j]
            thislist[j] = thislist[j+1] 
            thislist[j + 1] = t
print(thislist)
    


