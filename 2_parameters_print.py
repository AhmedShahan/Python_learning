'''
value=...., ....., .....
sep=
end=
file=
flash=
'''


### Using sep
print("Shahan", "Ahmed", 3.14, 54, True)
'''
Output: Shahan Ahmed 3.14 54 True

if we want to give comma or full stop or any symbol then use this (,./;'()*&^%$#@@!...... so on)
'''

print("Shahan", "Ahmed", 3.14, 54, True, sep='\t')


### Using end
print("Shahan")
print("Ahmed")
'''
It will print one line after another. Let say we want in a single line, ot tabbed after one line another instead off \n
'''
print("Shahan", end=",")
print("Shahan", end="-")
print("Shahan", end="/")
print("Shahan", end="&")
print("Shahan", end="\n")
print("Shahan", end="\t")
print("Ahmed")



