import sys

# enter python name.py Tammy in terminal
# enter python name.py Tammy K in terminal
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2: 
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few arguments") 
elif len(sys.argv) > 2: 
    sys.exit("Too many arguments")

    print("hello, my name is", sys.argv[1])


# enter python name.py Tammy K blob in terminal
for arg in sys.argv[1:]:
    print("hello my name is", arg)

for arg in sys.argv[1:-1]:
    print("hello my name is", arg)

