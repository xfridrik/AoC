file1 = open('in7.txt', 'r')

inp = [int(x) for x in file1.read().split(',')]

minfuel=0
for i in range(min(inp),max(inp)):
    fuel=0
    for c in inp:
        fuel=fuel+sum(range(1,(abs(c-i)+1)))
    if(i==min(inp)):
        minfuel=fuel
    elif(fuel<minfuel):
        minfuel=fuel
print(minfuel)

