li=["seat1","seat2","seat3"]
lis=[]
unq=[]
flag=0


for i in range(3):
    enter=input(" ")
    lis.append(enter)
for i in li:
    if enter==i:
        flag+=1
if flag==0:
    print("Invalid")


for z in lis:
    if z in unq:
        unq.append(z)








for x in lis:
    if x not in unq:
        unq.append(x)
    else:
        print(x,"and",z,"is already in use")
        break












