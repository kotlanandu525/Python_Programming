st=input()
newstr=sorted(st)
dict={}
ans=""
for i,c in enumerate(newstr):
    dict[c]=dict.get(c,0)+1
print(dict)
for key,val in dict.items():
    ans+=str(key)+str(val)
print(ans)