def print_full_name(a, b):
    b = b+"!"
    print("Hello",a, b,"You just delved into python.");   
if __name__ == '__main__':
    first_name = input("First name")
    last_name = input("Last name")
    print_full_name(first_name, last_name)