# names = []

# for _ in range(3):
#    names.append(input("What's your name? "))

# for name in sorted(names):
#    print(f"hello, {name}")

name = input("What's your name? ")

# deletes old content and replaces with new name, overwriting 
# file = open("names.txt", "w")
# file = open("names2.txt", "a")
# adds newline 
with open("names2.txt", "a") as file: 
    file.write(f"{name}\n")
file.close()

with open("names2.txt", "r") as file:
    lines = file.readlines() 

for line in lines:
    print("hello,", line)
    # print("hello,", line, end="") takes out the new line after each name
    print("hello,", line.rstrip()) # takes out the new line after each name
file.close()

names = []
with open("names2.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
file.close()

with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")




