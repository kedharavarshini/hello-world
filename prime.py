r=int(input("enter no"))
i=1
j=0
while i<=r:
    if r%i==0:
        j+=1
    i+=1
if j==2:
    print("prime no")
else:
    print("not prime")
