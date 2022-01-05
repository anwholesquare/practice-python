#condition

#even or odd
x = input("Enter an integer number: ")
x = int(x)
if x % 2 == 0 :
    print("{} is an even number".format (x))
else :
    print("{} is an odd number".format(x))
    


#finding out the max number

x = input()
y = input()
z = input()

if x > y and x > z:
    print("max: {}".format(x))
elif y > x and y > z:
    print("max: {}".format(y))
else:
    print("max: {}".format(z))


#finding out the grade
mark = input("Enter your mark: ")
mark = int(mark)
if mark >= 80 and mark <= 100:
    print("4.0")
elif mark >= 75 and mark <= 79:
    print("3.75")
elif mark >= 70 and mark <= 74:
    print("3.5")
elif mark >= 65 and mark <= 69:
    print("3.25")
elif mark >= 60 and mark <= 64:
    print("3.00")
elif mark >= 55 and mark <= 59:
    print("2.75")
elif mark >= 50 and mark <= 54:
    print("2.5")
elif mark >= 45 and mark <= 49:
    print("2.25")
elif mark >= 40 and mark <= 44:
    print("2.00")
else:
    print("F")
