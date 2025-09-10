day1=["a@gmail.com","b@gmail.com","b@gmail.com","CD@gmail.com"]
day2=["g@gmail.com","f@gmail.com","a@gmail.com","Cg@gmail.com"]
day3=["x@gmail.com","a@gmail.com","f@gmail.com","CD@gmail.com","K@gmail.com"]
a,b,c=set(),set(),set()
for i in day1:
    a.add(i.lower())
for i in day2:
    b.add(i.lower())
for i in day3:
    c.add(i.lower())
total=set(a|b|c)
print("day1=",a)
print("day2=",b)
print("day3=",c)
print("total attendies=",len(total))
print("attendies of all 3 days ",a&b&c)
print("attendies of exactily one days ",a^b^c)
print("pair1=",a&b,"pair2=",b&c,"pair3=",a&c)
print("report--")
print("day1 count",len(a))
print("day2 count",len(b))
print("day3 count",len(c))