str="lingmpally123@.com"
char,dg,other=0,0,0
for s in str:
    if s.isalpha():
        char+=1
    elif s.isdigit():
        dg+=1
    else:
        other+=1
print("alphabets=",char,"digits=",dg,"others=",other)