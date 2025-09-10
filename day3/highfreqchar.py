st=input()

dict={}
ans=""
for i,c in enumerate(st):
    dict[c]=dict.get(c,0)+1
print(dict)

ans=max(dict.values())
for k,v in dict.items():
    if v==ans:
        print("highfrq character",k)