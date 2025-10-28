# a=input("Enter a number: ")
# print(a, type(a))

# b=input("Enter a String: ")
# print(b, type(b))

'''
Enter a number: 20
20 <class 'str'>
Enter a String: shahan
shahan <class 'str'>
BOTH SHOWS the string 
'''

### Type cast
# a=int(input("Enter a number: "))
# print(a, type(a))



##### multiple input type cast
## Method 1
# a,b=input("Enter 2 numbers: ").split()
# a=int(a)
# b=int(b)
# print(a, type(a))
# print(b, type(b))


# ## Methodd 2
# a,b=map(int,input("Enter 2 numbers: ").split())
# print(a,type(a))
# print(b,type(b))


## list o homogenous int numebrs take

a=list(map(int,input("Enter numbers: ").split()))
print(a, type(a))