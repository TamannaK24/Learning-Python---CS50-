# Ask user for their name
name = input("What's your name? ")

# if the user presses space bar a ton and enters name, this removes the spaces
name = name.strip()
# strips space from left or right  
name = name.lstrip()
name = name.rstrip() 

# capitalize user's name 
name = name.capitalize() 

# capitalizes user's first and last name 
name = name.title() 

# splits users first and last name into two variables
first, last = name.split(" ")

# simplifying code
name = name.strip().title()

# Say hello to user
print("Hello,")
print(name)
print("Hello, " + name) 
print("Hello,", name) 
print("Hello, ", end="")
print(name)
print("Hello, ", end="???")
print(name)
print("Hello,",name,sep='???')
print("Hello,",name,sep="???")
print('Hello, "friend"')
print("Hello \"friend\"")
print(f"Hello {name}")

# creating own functions
def hello(to): 
    print("hello,", to)

hello(name)

