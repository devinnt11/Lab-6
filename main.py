def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def password_encoder(password):
    result = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        result += str(new_digit)
    return result


def decode(encoded_password):
    decoder_password = ""

    for digit in encoded_password:
        # Convert the character to an integer and shift it down by 3
        decoded_digit = str(int(digit) - 3)
        decoder_password += decoded_digit

    return decoder_password

def main():
    run_code = True
    while run_code:
        print_menu()
        menu_option = input("Please enter an option:")
        if menu_option == "1":
            password = input("Please enter your password to encode:")
            print(password_encoder(password))
        elif menu_option =="2":
            print(f"The encoded password is {password}, and the original password is {decoder(password)}")
        elif menu_option == "3":
            break


if __name__ == "__main__":
    main()


