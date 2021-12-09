file1 = open('in9.txt', 'r')

inp = [(x) for x in file1.read().split('\n')]
arr=[]
done=[]
line=0
for line in inp:
    linenums=[]
    d=[]
    for num in line:
        linenums.append(int(num))
        d.append(False)
    arr.append(linenums)
    done.append(d)
    
def basins(i,j,arr):
    count=1
    if(done[i][j]==True):
        return 0
    else:
        done[i][j]=True
    if(i-1>=0): #up
        if(arr[i-1][j]<9):
            count+=basins(i-1,j,arr)
    if(j-1>=0): #left
        if(arr[i][j-1]<9):
            count+=basins(i,j-1,arr)
    if(i+1<len(arr)): #down
        if(arr[i+1][j]<9):
            count+=basins(i+1,j,arr)
    if(j+1<len(arr[i])): #right
        if(arr[i][j+1]<9):
            count+=basins(i,j+1,arr)
    return(count)

risk=0
bas=[]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if(i-1>=0): #up
            if(arr[i-1][j]<=arr[i][j]):
                continue
        if(j-1>=0): #left
            if(arr[i][j-1]<=arr[i][j]):
                continue
        if(i+1<len(arr)): #down
            if(arr[i+1][j]<=arr[i][j]):
                continue
        if(j+1<len(arr[i])): #right
            if(arr[i][j+1]<=arr[i][j]):
                continue
        risk=risk+1+arr[i][j]
        bas.append(basins(i,j,arr))
print(risk)
bas.sort()
print(bas[len(bas)-1]*bas[len(bas)-2]*bas[len(bas)-3])
    
