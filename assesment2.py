n=int(input("enter the number of elements required"))
fib=[0,1]
i=2
while i<n:
    x=fib[i-1]+fib[i-2]
    fib.append(x) 
    i=i+1
print("the fibonacci series is:") 

for index in fib:
    print(index)
