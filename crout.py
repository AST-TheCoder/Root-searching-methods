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

#Finding the elements of L & U

a1=a
a2=b/a1
a3=c/a1

b1=u
b2=v-b1*a2
b3=(w-b1*a3)/b2

c1=x
c2=y-c1*a2
c3=z-c1*a3-c2*b3

#Finding the elemnts of Y

y1=p/a1
y2=(q-b1*y1)/b2
y3=(r-c1*y1-c2*y2)/c3

#Finding answers

ans3=y3
ans2=y2-b3*ans3
ans1=y1-a2*ans2-a3*ans3

print("The Value of x is",ans1)
print("The Value of y is",ans2)
print("The Value of z is",ans3)