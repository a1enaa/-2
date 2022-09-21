import math
y=0.000075
x=-4.5
z=-84.5
a=9+pow(x-y,2)
b=a**(1/3)
c=pow(math.e,abs(x-y))
f=c*pow(math.tan(z),3)
d=x**2+y**2+2
s=(b/d)-f
print(s)
