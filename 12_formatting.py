## Method 1: % (Ol style as like c)
'''
%s---> ffor string
%f---> for float
%dd--> for decimal or integer
'''

name="Shahan"
age=27
cgpa=3.8

# print("I am %s and I am %d years old also my CGPA is %f"%(age, name, cgpa))

## Method 2

print("I am {} and I am {} years old also my CGPA is {}".format(name, age, cgpa))
print("I am {1} and I am {0} years old also my CGPA is {2}".format(age, name, cgpa))
print("I am {n} and I am {a} years old also my CGPA is {cg}".format(a=age, n=name, cg=cgpa))

