a=[[8,5,4,-4],[9,7,5,18]]
for i in range(len(a)):
        min=a[i][0]
        for j in range(1,len(a[i])):
            if a[i][j]<min:
                min=a[i][j]
        a[i].remove(min)
        a[i].insert(0,min)
print(a)