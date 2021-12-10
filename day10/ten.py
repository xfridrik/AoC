file1 = open('in10.txt', 'r')

inp = [(x) for x in file1.read().split('\n')]
err=0
comp=[]
for line in inp:
    brack=[]
    wrong=False
    for char in line:
        if(char=="("):
            brack.append(char)
        if(char==")"):
            if(not(brack[len(brack)-1]=="(")):
                err+=3
                wrong=True
            brack.pop(len(brack)-1)
            
        if(char=="["):
            brack.append(char)
        if(char=="]"):
            if(not(brack[len(brack)-1]=="[")):
                err+=57
                wrong=True
            brack.pop(len(brack)-1)
            
        if(char=="<"):
            brack.append(char)
        if(char==">"):
            if(not(brack[len(brack)-1]=="<")):
                err+=25137
                wrong=True
            brack.pop(len(brack)-1)
            
        if(char=="{"):
            brack.append(char)
        if(char=="}"):
            if(not(brack[len(brack)-1]=="{")):
                err+=1197
                wrong=True
            brack.pop(len(brack)-1)
    if(not wrong):
        vys=0
        for i in reversed(brack):
            vys=vys*5
            if i=="(":
                vys+=1
            if i=="[":
                vys+=2
            if i=="{":
                vys+=3
            if i=="<":
                vys+=4
        comp.append(vys)

comp.sort()
print(len(comp))
print(err)
print(comp[int(len(comp)/2)])
