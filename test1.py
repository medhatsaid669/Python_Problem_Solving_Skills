def print_menu():
    while True:
        print('\n\nMenu:')
        print('Enter 1 to add 2 numbers')
        print('Enter 2 to subtract 2 numbers')
        print('Enter 3 to end the program')

        user_inp = input('\nEnter choice from 1 to 3: ')

        if user_inp not in '123':
            print('Invalid Input...Try again')
            continue
        else:
            return user_inp



