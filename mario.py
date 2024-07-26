def main():
    print_row(4)

def print_row(width):
    print("?" * width) 

def print_square(size):
    for i in range(size): 
        for j in range(size):
            print("#", end="")
        print()

def print_square2(size):
    for i in range(size):
        print("#" * size)
        print_row(size)

def print_row(width):
    print("#" * width)
    

main() 

