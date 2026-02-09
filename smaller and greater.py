a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(greatest)
