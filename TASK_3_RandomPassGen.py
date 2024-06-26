import random


def generate_password(length, use_capital, use_numbers, use_symbols, capital_len=0, numbers_len=0, symbols_len=0):
    # Base character set
    li = 'abcdefghijklmnopqrstuvwxyz'
    licap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    linum = '1234567890'
    symbols = '!@#$%^&*()_+[]{};:"|,.<>?/`~'

    # Validate the lengths
    if capital_len + numbers_len + symbols_len > length:
        print(f"The total specified characters exceed the desired password length of {length}.")
        return None
    
    # Collecting the necessary characters
    password_chars = random.choices(li, k=length - capital_len - numbers_len - symbols_len)
    
    if use_capital:
        password_chars += random.choices(licap, k=capital_len)
    if use_numbers:
        password_chars += random.choices(linum, k=numbers_len)
    if use_symbols:
        password_chars += random.choices(symbols, k=symbols_len)
    
    # Shuffle to ensure randomness
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    length = int(input('Enter the length of the password: '))
    
    ask_capital = input('Do you want to include any capital letters (y/n): ').lower() == 'y'
    ask_numbers = input('Do you want to include any numbers (y/n): ').lower() == 'y'
    ask_symbols = input('Do you want to include any special symbols (y/n): ').lower() == 'y'
    
    capital_len = numbers_len = symbols_len = 0
    
    if ask_capital:
        capital_len = int(input('Enter the total number of capital letters in the password: '))
    if ask_numbers:
        numbers_len = int(input('Enter the total number of numbers in the password: '))
    if ask_symbols:
        symbols_len = int(input('Enter the total number of special symbols in the password: '))
    
    password = generate_password(length, ask_capital, ask_numbers, ask_symbols, capital_len, numbers_len, symbols_len)
    
    if password:
        print(f"Your generated password is: {password}")

main()
