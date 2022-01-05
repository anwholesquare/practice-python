#Input

#input for a variable
x = input("Enter a value: ")
print(x)

#input type checking
y = "55"
print(isinstance(y, int))
print(isinstance(y, float))
print(isinstance(y, str))

#input digit only

z = 'ab'
flag = True
while flag:
    try:
        z = input ("Enter an integer value: ")
        z = int (z)
    except:
        continue;
    flag = False

print(z)


#input float only

r = 'a'
flag = True
while flag:
    try:
        r = input("Enter a floating value of R: ")
        r = float(r)
    except:
        continue
    flag = False
print(r)
