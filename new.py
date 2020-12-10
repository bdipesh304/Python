from math import*
print("Input a,b,c by comparing with eqn ax+by+c")
a=float(input("a ="))
b= float(input("b ="))
c= float(input("c ="))
print("Now enter passing point ")
x=float(input('x ='))
y=float(input("y ="))
d=float(a*x+b*y +c)
e = float(sqrt(a*a+b*b))
f=float((d/e))
g= float(-(f))
if f>0 :
    print(f)
elif f<0 :
    print(g)1


