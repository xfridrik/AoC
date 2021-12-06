file1 = open('in6.txt', 'r')

inp = [int(x) for x in file1.read().split(',')]

sample=[]
sample256=[]
fishes128=[]
sa=[]
suma=0

#sample fishes for 128 days
for j in range(9):
    sa=[]
    sa.append(j)
    for i in range(128):
        k=0
        for fish in sa:
            if(fish==0):
                sa.append(9)
                sa[k]=7
            sa[k]=sa[k]-1
            k=k+1
    sample.append(len(sa))
    fishes128.append(sa)

#sample fishes for 256 days
for j in range(9):
    sumfish=0
    for fish in fishes128[j]:
        sumfish=sumfish+sample[fish]
    sample256.append(sumfish)

#sum input fishes with 256 days sample
for fish in inp:
    suma=suma+sample256[fish]

print(suma)
