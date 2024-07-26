x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y) 
print(z) 

x = int(input("What's x? "))
y = int(input("What's y? "))
print(x+y) 

print(int(input("What's x? ")) + int(input("What's y? ")))

x = float(input("What's x? "))
y = float(input("What's y? "))
print(round(x+y))
z = round(x+y)
print(round(z))
# formats number with , 
print(f"{z:,}")

z = round(x / y, 2)  
print(z) 

# prints up to 2 decimal places
z = x / y
print(f"{z:.2f}")

print(f"hello, {name}")

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False 

def is_even2(n):
    return (n % 2 == 0)

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


