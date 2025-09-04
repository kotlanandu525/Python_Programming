amt=int(input("enter thre amount="))

def evaluate(a):
    res=0
    if(a>=2000):
        res+=a//2000
        r2000=a//2000
        a=a-res*2000
        print(" 2000=",r2000)
    if(a>=500):
        res+=a//500
        r500=a//500
        a=a-r500*500
        print(" 500=",r500)
    if(a>=200):
        res+=a//200
        r200=a//200
        a=a-(r200)*200
        print(" 200=",r200)
    if(a>=100):
        res+=a//100
        r100=a//100
        a=a-(r100)*100
        print(" 100=",r100)
    if(a>=50):
        res+=a//50
        r50=a//50
        a=a-(r50)*50
        print(" 50=",r50)
    return res
print("min no of notes in a given amount",evaluate(amt))
    