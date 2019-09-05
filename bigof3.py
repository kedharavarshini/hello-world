p=int(input("enter p value"))
q=int(input("enter q value"))
r=int(input("enter r value"))
if p>q and p>r:
    print(p,"is largest of  three nos")
    print("first large number is",p)
    if q>r:
        print("second large number is",q)
        print("third large number is",r)
    else:
        print("second large no is",r)
        print("third large no is",q)
elif q>p and q>r:
    print(q,"is large of three nos")
    print("first large number is",q)
    if p>r:
        print("second large no is",p)
        print("third large no is",r)
    else:
        print("second large no is",r)
        print("third large no is ",p)
else:
    print(r,"is largre large of three nos")
    print("first large no is",r)
    if p>q:
        print("second large no is",p)
        print("third largr is",q)
    else:
        print("second large no is",q)
        print("third large no is",p)
