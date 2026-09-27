from numpy import *

val = array([1,2,3,4.5,'a'])

for x in val:
    print(x,end=',')
print("\n")

# linspace -- to divide in equal parts

# linspace = linspace(starting,ending,how many parts)

a = linspace(10,20,5)
for x in a:
    print(x,end=',')
print("\n")

# arange -- difference
# arange = arange(starting,ending,difference)

b = arange(10,20,5)

for x in b:
    print(x,end=',')
print("\n")

# we can print zeros using zeros

c = zeros(10)

for x in c:
    print(x,end=',')
print("\n")

d = ones(10)
print(d)

# any other number we use full

# e = full(how many,which number)

e = full(10,5)
print(e)

# --------we can make multi diamention array---------

# zero dimention

zero = array(10)
print(zero)

# one dimention

one = array([1,2,3,4])

print(one)

# two  diamention
# collection of one diamenton array

two = array([[1,2,3],[4,5,6],[3,4,5]])

print(two)

# three diamention array
# collecton of two diamention array

three= array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three)