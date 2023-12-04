import random
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the required length of the Password: "))
    include_letters = input("Should it include Letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Should it include Numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Should it include Symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print("\n\nDesired Generated Password: ", password)
    print("\nThankyou for using us! Hope you like the service...\n")

main()
