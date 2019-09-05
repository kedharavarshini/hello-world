#s="abc234byg67"
s=input("enter string")
sum=0
g=len(s)
for i in range (g):
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)
