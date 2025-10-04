x=10
y=10
print(id(x))
print(id(y))



### Dynamic binding
x=10
print(type(x))
x="Shahan"
print(type(x))
x=3.14416
print(type(x))


### special syntex in variable assignemnt

# In a sinle line declearation
x="Shahan"; y=1001; z=3.1416
print(x)
print(y)
print(z)

# same value multiple variable
a=b=c=10
print(a)
print(b)
print(c)


# *** Most useful variable assign
a,b,c=5,6,7
print(a)
print(b)
print(c)
