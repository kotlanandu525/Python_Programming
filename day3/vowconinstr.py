str="lingmpally123@.com"
vow="aeiouAEIOU"
vcnt,ocnt,concnt=0,0,0
for s in str:
    if s in vow:
        vcnt+=1
    elif s not in vow and s.isalpha():
        concnt+=1
    else:
        ocnt+=1
print("vowel cnt=",vcnt,"consonent cnt",concnt,"others cnt=",ocnt)

    