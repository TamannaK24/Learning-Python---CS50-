def main():
    meow(3)

i = 3
while i != 0:
    print("meow")
    i = i - 1

i = 1
while i <= 3:
    print("meow")
    i = i + 1

i = 0
while i < 3:
    print("meow")
    i = i + 1

for i in [0,1,2]:
    print("meow")

for i in range(3):
    print("meow") 

for _ in range(3):
    print("meow") 

print("meow\n" * 3)

print("meow\n" * 3, end="")

n = int(input("What's n? "))
if n < 0:
    n = int(input("What's n? "))
    if n < 0:
        n = int(input())

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break 

while True:
    n = int(input("What's n? "))
    if n > 0:
        break 

for _ in range(n): 
    print("meow")


def meow(n): 
    for _ in range(n):
        print("meow") 

main()
