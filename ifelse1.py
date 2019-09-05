user=44
password=66
a=int(input("enter user"))
if(user==a):
    r=int(input("enter password"))
    if r==password:
        print("welcome")
    else:
        print("invalid password")
else:
    print("invalid user")
