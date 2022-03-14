from pickle import TRUE

print()
a1=float(input("Co-efficient of x1 in maximize function: "))
a2=float(input("Co-efficient of x2 in maximize function: "))
print()
b1=float(input("Co-efficient of x1 in condition 1: "))
b2=float(input("Co-efficient of x2 in condition 1: "))
b3=float(input("Range of condition 1: "))
print()
c1=float(input("Co-efficient of x1 in condition 2: "))
c2=float(input("Co-efficient of x2 in condition 2: "))
c3=float(input("Range of condition 2: "))
print()

p1=a1
p2=a2
p3=0
p4=0

q1=b1
q2=b2
q3=1
q4=0
q5=b3

r1=c1
r2=c2
r3=0
r4=1
r5=c3

ans=0

f1=0
f2=0

s1=0
s2=0
s3=0
s4=0
s5=0

t1=0
t2=0
t3=0
t4=0
t5=0

while TRUE:
    z1=f1*q1+f2*r1
    z2=f1*q2+f2*r2
    z3=f1*q3+f2*r3
    z4=f1*q4+f2*r4
    ans=f1*q5+f2*r5

    flag=0
    x1=p1-z1
    x2=p2-z2
    x3=p3-z3
    x4=p4-z4

    if x1<=0 and x2<=0 and x3<=0 and x4<=0:
        print("The maximum value of z is",ans)
        exit()

    if x1>=x2 and x1>=x3 and x1>=x4:
        if q5/q1<=r5/r1:
            f1=p1
            s1=q1/q1
            s2=q2/q1
            s3=q3/q1
            s4=q4/q1
            s5=q5/q1

            t1=r1-(q1*r1)/q1
            t2=r2-(q2*r1)/q1
            t3=r3-(q3*r1)/q1
            t4=r4-(q4*r1)/q1
            t5=r5-(q5*r1)/q1
        else:
            f2=p1
            t1=r1/r1
            t2=r2/r1
            t3=r3/r1
            t4=r4/r1
            t5=r5/r1

            s1=q1-(r1*q1)/r1
            s2=q2-(r2*q1)/r1
            s3=q3-(r3*q1)/r1
            s4=q4-(r4*q1)/r1
            s5=q5-(r5*q1)/r1
    elif x1<=x2 and x2>=x3 and x2>=x4:
        if q5/q2<=r5/r2:
            f1=p2
            s1=q1/q2
            s3=q3/q2
            s2=q2/q2
            s4=q4/q2
            s5=q5/q2

            t1=r1-(q1*r2)/q2
            t2=r2-(q2*r2)/q2
            t3=r3-(q3*r2)/q2
            t4=r4-(q4*r2)/q2
            t5=r5-(q5*r2)/q2
        else:
            f2=p2
            t1=r1/r2
            t2=r2/r2
            t3=r3/r2
            t4=r4/r2
            t5=r5/r2

            s1=q1-(r1*q2)/r2
            s2=q2-(r2*q2)/r2
            s3=q3-(r3*q2)/r2
            s4=q4-(r4*q2)/r2
            s5=q5-(r5*q2)/r2
    elif x1<=x3 and x2<=x3 and x3>=x4:
        if q5/q3<=r5/r3:
            f1=p3
            s1=q1/q3
            s2=q2/q3
            s3=q3/q3
            s4=q4/q3
            s5=q5/q3

            t1=r1-(q1*r3)/q3
            t2=r2-(q2*r3)/q3
            t3=r3-(q3*r3)/q3
            t4=r4-(q4*r3)/q3
            t5=r5-(q5*r3)/q3
        else:
            f2=p3
            t1=r1/r3
            t2=r2/r3
            t3=r3/r3
            t4=r4/r3
            t5=r5/r3

            s1=q1-(r1*q3)/r3
            s2=q2-(r2*q3)/r3
            s3=q3-(r3*q3)/r3
            s4=q4-(r4*q3)/r3
            s5=q5-(r5*q3)/r3
    else:
        if q5/q4<=r5/r4:
            f1=p4
            s1=q1/q4
            s2=q2/q4
            s3=q3/q4
            s4=q4/q4
            s5=q5/q4

            t1=r1-(q1*r4)/q4
            t2=r2-(q2*r4)/q4
            t3=r3-(q3*r4)/q4
            t4=r4-(q4*r4)/q4
            t5=r5-(q5*r4)/q4
        else:
            f2=p4
            t1=r1/r4
            t2=r2/r4
            t3=r3/r4
            t4=r4/r4
            t5=r5/r4

            s1=q1-(r1*q4)/r4
            s2=q2-(r2*q4)/r4
            s3=q3-(r3*q4)/r4
            s4=q4-(r4*q4)/r4
            s5=q5-(r5*q4)/r4
    q1=s1
    q2=s2
    q3=s3
    q4=s4
    q5=s5

    r1=t1
    r2=t2
    r3=t3
    r4=t4
    r5=t5