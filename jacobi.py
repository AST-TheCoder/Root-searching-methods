print()
a=float(input("Co-efficient of x in equation 1: "))
b=float(input("Co-efficient of y in equation 1: "))
c=float(input("Co-efficient of z in equation 1: "))
p=float(input("Constant of equation 1: "))
print()
u=float(input("Co-efficient of x in equation 2: "))
v=float(input("Co-efficient of y in equation 2: "))
w=float(input("Co-efficient of z in equation 2: "))
q=float(input("Constant of equation 2: "))
print()
x=float(input("Co-efficient of x in equation 3: "))
y=float(input("Co-efficient of y in equation 3: "))
z=float(input("Co-efficient of z in equation 3: "))
r=float(input("Constant of equation 3: "))
print()

#Check Conditions
flag=0
perm=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i==j or i==k or j==k:
                continue
            temp=0
            if i==0 and abs(b)+abs(c)<=abs(a) and temp==0:
                temp=1
            if i==1 and abs(a)+abs(c)<=abs(b) and temp==0:
                temp=1
            if i==2 and abs(b)+abs(a)<=abs(c) and temp==0:
                temp=1

            if j==0 and abs(v)+abs(w)<=abs(u) and temp==1:
                temp=2
            if j==1 and abs(u)+abs(w)<=abs(v) and temp==1:
                temp=2
            if j==2 and abs(u)+abs(v)<=abs(w) and temp==1:
                temp=2
            
            if k==0 and abs(y)+abs(z)<=abs(x) and temp==2:
                temp=3
            if k==1 and abs(x)+abs(z)<=abs(y) and temp==2:
                temp=3
            if k==2 and abs(x)+abs(y)<=abs(z) and temp==2:
                temp=3

            if temp==3:
                flag=1
                perm=k*100+j*10+i

if flag==0:
    print("Roots can't be found by Gauss-Jacobi method.")
    exit()

ans1=0
ans2=0
ans3=0

for i in range(100):
    temp1=0
    temp2=0
    temp3=0

    id=perm%10
    if id==0:
        temp1=(p-b*ans2-c*ans3)/a
    if id==1:
        temp2=(p-a*ans1-c*ans3)/b
    if id==2:
        temp3=(p-a*ans1-b*ans2)/c

    id=int(perm/10)%10
    if id==0:
        temp1=(q-v*ans2-w*ans3)/u
    if id==1:
        temp2=(q-u*ans1-w*ans3)/v
    if id==2:
        temp3=(q-u*ans1-v*ans2)/w

    id=int(perm/100)%10
    if id==0:
        temp1=(r-y*ans2-z*ans3)/x
    if id==1:
        temp2=(r-x*ans1-z*ans3)/y
    if id==2:
        temp3=(r-x*ans1-y*ans2)/z

    ans1=temp1
    ans2=temp2
    ans3=temp3

print("The Value of x is",ans1)
print("The Value of y is",ans2)
print("The Value of z is",ans3)