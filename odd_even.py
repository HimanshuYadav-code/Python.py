def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
        # return True if n % 2 == 0 else False
        # or return n % 2 == 0
    else:
        return False
    
main()