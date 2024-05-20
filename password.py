import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = get_password_length()
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
