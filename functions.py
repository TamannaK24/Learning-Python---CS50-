def main():
    name = input("What's your name? ")
    hello(name) 
    hello() 

    x = int(input("What's x? ")) 
    print("x squared is", square(x)) 

    if name == "Harry" or name == "Hermoine" or name == "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("Who?") 

    match name:
        case "Harry":
            print("Gryffindor")
        case "Hermione": 
            print("Gryffindor")
        case "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

    match name:
        case "Harry" | "Hermione" | "Ron": 
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
            



def hello(to="world"):
    print("hello,", to)

def square(n):
    return n * n
    # return n ** 2 or pow(n, 2) which is n^2
 

# name doesn't exist in the scope
# def hello():
#    print("hello,", name)

main() 