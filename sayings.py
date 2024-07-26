def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# ensures main isn't automatically called
if __name__ == "__main__":
    main()
