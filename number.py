def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    print("x squared is", square(x))

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def square(n):
    # mistake on purpose
    return n + n 

if __name__ == "__main__": 
    main()