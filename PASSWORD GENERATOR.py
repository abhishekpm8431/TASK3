import random
import string

def generate_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters  # Only letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits  # Letters and digits
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, and symbols
    else:
        print("Invalid complexity level. Please choose 1, 2, or 3.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    complexity = input("Choose complexity level (1: Letters, 2: Letters + Digits, 3: Letters + Digits + Symbols): ")

    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()