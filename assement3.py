n=int(input("enter the number of elements in list"))
numlist=[]
print("enter elements one by one")
for i in range(0,n):
    x=int(input())
    numlist.append(x)

for i in numlist:
    if i>0:
        print(i)
    else:
        continue
    
    
