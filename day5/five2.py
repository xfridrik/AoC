file1 = open('input5.txt', 'r')
Lines = file1.readlines()
 
a=[]
for line in Lines:
    a.append(line)
w=""

nums=[]
pair=[]
line=[]
for l in a:
    pair=[]
    for n in l:
        if (n== ','):
            pair.append(int(w))
            w=""
        elif (n==" " or n==">"):
            w=w
        elif(n=="-"):
            pair.append(int(w))
            line.append(pair)
            w=""
            pair=[]
        elif (n=='\n'):
            pair.append(int(w))
            line.append(pair)
            nums.append(line)
            line=[]
            pair=[]
            w=""
        else:
            w=w+n
    pair=[]
    w=""

arr=[]
for i in range(1000):
    row=[]
    for j in range(1000):
        row.append(0)
    arr.append(row)
for line in nums:
    if(line[0][0]==line[1][0]):
        if(line[0][1]<line[1][1]):
            y1=line[0][1]
            y2=line[1][1]
        else:
            y2=line[0][1]
            y1=line[1][1]
        for i in range(y1,y2+1):
            arr[i][line[0][0]]=arr[i][line[0][0]]+1
    elif(line[0][1]==line[1][1]):
        if(line[0][0]<line[1][0]):
            x1=line[0][0]
            x2=line[1][0]
        else:
            x2=line[0][0]
            x1=line[1][0]
        for i in range(x1,x2+1):
            arr[line[1][1]][i]=arr[line[1][1]][i]+1
    elif(abs(line[0][0]-line[1][0]) == abs(line[0][1]-line[1][1])):
        if(line[0][1]<=line[1][1]):
            if(line[0][0]<=line[1][0]):
                y1=line[0][1]
                x1=line[0][0]
                for i in range(abs(line[0][0]-line[1][0])+1):
                    arr[y1+i][x1+i]=arr[y1+i][x1+i]+1
        if(line[0][1]<=line[1][1]):
            if(line[0][0]>line[1][0]):
                y1=line[0][1]
                x1=line[0][0]
                for i in range(abs(line[0][0]-line[1][0])+1):
                    arr[y1+i][x1-i]=arr[y1+i][x1-i]+1
        if(line[0][1]>line[1][1]):
            if(line[0][0]<=line[1][0]):
                y1=line[0][1]
                x1=line[0][0]
                for i in range(abs(line[0][0]-line[1][0])+1):
                    arr[y1-i][x1+i]=arr[y1-i][x1+i]+1
        if(line[0][1]>=line[1][1]):
            if(line[0][0]>=line[1][0]):
                y1=line[0][1]
                x1=line[0][0]
                for i in range(abs(line[0][0]-line[1][0])+1):
                    arr[y1-i][x1-i]=arr[y1-i][x1-i]+1
            
sum=0
for i in range(1000):
    for j in range(1000):
        if(arr[i][j]>1):
            sum=sum+1
print(sum)
