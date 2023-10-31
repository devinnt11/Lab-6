def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    result = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        result += str(new_digit)
    return result
def main():
    run_code = True
    while run_code:
        print_menu()
        menu_option = input("Please enter an option:")
        if menu_option == "1":
            password = input("Please enter your password to encode:")
            print(encoder(password))
        elif menu_option =="2":
            print(f"The encoded password is {password}, and the original password is {decoder(password)}")
        elif menu_option == "3":
            break


if __name__ == "__main__":
    main()


