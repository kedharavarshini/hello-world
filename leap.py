r=int(input("enter year"))
if r%400==0 or(r%4==0 and r%100!=0):
    print("leap year")
else:
    print("non leap year")
