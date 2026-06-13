"""Library System Project

Background
● Many libraries have a library system
○ Helps to add books and searching for them
○ Maintains information about the borrowed books
● We will create a simple version of this classical system
● The main user of the system is an admin
○ Who might add a book, user or perform some relevant operation
○ You don’t need to provide login/logout functionalities in this console system
● The system starts with a menu
○ It shows all possible choices
○ The admin selects a choice.
■ Some operation is performed
○ Then the main menu is listed again
The menu
● Take a minute to read these choices
Books operations: Adding a book
● Every system needs data. The core data here is the book and users
● The admin needs to be able to add books
● Each book has the following information
○ id, name and quantity
○ Example: 101, Cpp How To Program, 7
■ We have 7 copies for book Cpp How To Program
■ The book ID is 101
Books operations: Searching for a book
● Searching your database of books is a typical operation
● We will search the system using the book name.
● Instead of the complete book name, we will allow a prefix
○ Prefix: The first letters of a word
● Assume we have 3 books in the system, their names:
○ CppHowToProgram, CppForDummies, CppForAdvancedLevels, CoreJava
● Query
○ Cpp ⇒ CppHowToProgram, CppForDummies, CppForAdvancedLevels
○ CppFo ⇒ CppForDummies, CppForAdvancedLevels
○ Core ⇒ CoreJava
○ Java ⇒ Nothing
Book Operations: Listing books
● Another typical operations is to just list all books in the system
Book Operations: Listing users borrowed a book
● Given that several users may borrow a book, the admins may want to know
who borrowed what.
○ Remember we have several copies per book.
● Input: Book Name
○ E.g. Math1
● Output: list of the user names who borrowed the book
○ E.g. Mostafa, John, Mark, Ali
User Operations: Add a user
● Each user has only an Id and name
● We only request 2 operations
○ Borrowing a book
○ Returning a book
User Operation: Borrow a book
● Borrowing books is a repetitive scenario in libraries
● Each book already has a specific number of copies (the quantity)
● To borrow a book, this quantity must be  > 0
○ Otherwise, this book can’t be borrowed
● After borrowing, the quantity must be decreased
● The admin enters the user name and the book name
○ If there are enough quantity of the book, the system does the following:
■ Mark that this user borrowed a copy
■ Decrease the quantity with 1
○ If there is no available copies, the system notifies the admin
User Operation: Return a book
● Same logic, but this time the system does the reverse:
○ Mark that the user returned a copy
○ Increment the current quantity”"""

def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


class Book:
    def __init__(self, name, id, total_quantity):
        self.name = name
        self.id = id
        self.total_quantity = total_quantity
        self.total_borrowed = 0

    def borrow(self):
        if self.total_quantity - self.total_borrowed == 0:
            return False
        self.total_borrowed += 1
        return True

    def return_copy(self):
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self):
        return f'Book name: {self.name:20} - id: {self.id} - total quantity: {self.total_quantity} - ' \
               f'total borrowed: {self.total_borrowed}'


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def is_borrowed(self, book):
        # In practice: this is wrong as it compares memory addresses. Later we will make it proper
        #return book in self.borrowed_books
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False


    def return_book(self, book):
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]
                break

    def simple_repr(self, is_detailed = False):
        ret = f'User name: {self.name:15} - id: {self.id}'
        if is_detailed and self.borrowed_books:
            ret += '\n\tBorrowed books:\n'
            for book in self.borrowed_books:
                ret += f'\t{str(book)}\n'
        return ret

    def __repr__(self):
        return self.simple_repr(True)



class BackendManger:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, name, id, total_quantity):
        self.books.append(Book(name, id, total_quantity))

    def get_books_with_prefix(self, prefix):
        return [book for book in self.books if book.name.startswith(prefix)]

    def add_user(self, name, id):
        self.users.append(User(name, id))

    def get_user_by_name(self, name):
        for user in self.users:
            if name == user.name:
                return user
        return None

    def get_book_by_name(self, name):
        for book in self.books:
            if name == book.name:
                return book
        return None

    def borrow_book(self, user_name, book_name):
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return False

        if book.borrow():
            user.borrow(book)
            return True
        return False

    def return_book(self, user_name, book_name):
        user = self.get_user_by_name(user_name)
        book = self.get_book_by_name(book_name)

        if user is None or book is None:
            return

        if user.is_borrowed(book):
            book.return_copy()
            user.return_book(book)
        else:
            print('This user did not borrow this book')

    def get_users_borrowed_book(self, book_name):
        book = self.get_book_by_name(book_name)

        if book is None:
            return []

        return [user for user in self.users if user.is_borrowed(book)]





class FrontendManager:
    def __init__(self):
        self.backend = BackendManger()
        self.add_dummy_data()

    def print_menu(self):
        print('\nProgram Options:')

        messages = [
            'Add book',
            'Print library books',
            'Print books by prefix',
            'Add user',
            'Borrow book',
            'Return book',
            'Print users borrowed book',
            'Print users',
        ]
        messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))

        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def add_dummy_data(self):
        self.backend.add_book('math4', '100', 3)
        self.backend.add_book('math2', '101', 5)
        self.backend.add_book('math1', '102', 4)
        self.backend.add_book('math3', '103', 2)
        self.backend.add_book('prog1', '201', 3)
        self.backend.add_book('prog2', '202', 3)

        self.backend.add_user('mostafa', '30301')
        self.backend.add_user('ali', '50501')
        self.backend.add_user('noha', '70701')
        self.backend.add_user('ashraf', '90901')

        self.backend.borrow_book('mostafa', 'math3')
        self.backend.borrow_book('noha', 'math3')



    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.print_name_prefix()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed_book()
            elif choice == 8:
                self.print_users()
            else:
                break

    def add_book(self):
        print('\nEnter book info:')
        name = input('Book name: ')
        id = input('Book id: ')
        total_quantity = int(input('Total quantity: '))
        self.backend.add_book(name, id, total_quantity)

    def print_books(self):
        # Let's "delegate" the call to a general function
        self.print_name_prefix(just_print_all=True)

    def print_name_prefix(self, just_print_all = False):
        prefix = ''
        if not just_print_all:
            prefix = input('Enter book name prefix: ')

        books = self.backend.get_books_with_prefix(prefix)
        books_str = '\n'.join([str(book) for book in books])
        print(books_str)

    def add_user(self):
        print('\nEnter user info:')
        name = input('User name: ')
        id = input('User id: ')
        self.backend.add_user(name, id)

    def read_user_name_and_book_name(self, trials = 3):
        """
        The function tries to read valid user name and password up to #trials
        If finally correct, it returns the read names, otherwise None, None
        """
        trials += 1

        while trials > 0:
            trials -= 1
            print('Enter user name and book name')

            user_name = input('User name: ')
            if self.backend.get_user_by_name(user_name) is None:
                print('Invalid user name!')
                continue

            book_name = input('Book name: ')
            if self.backend.get_book_by_name(book_name) is None:
                print('Invalid book name!')
                continue

            return user_name, book_name

        print('You did several trials! Try later.')
        return None, None


    def borrow_book(self):
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        if not self.backend.borrow_book(user_name, book_name):
            print('Failed to borrow the book')

    def return_book(self):
        user_name, book_name = self.read_user_name_and_book_name()

        if user_name is None or book_name is None:
            return

        self.backend.return_book(user_name, book_name)

    def print_users_borrowed_book(self):
        book_name = input('Book name: ')
        if self.backend.get_book_by_name(book_name) is None:
            print('Invalid book name!')
        else:
            users_lst = self.backend.get_users_borrowed_book(book_name)

            if not users_lst:
                print('\nNo one borrowed this book')
            else:
                print('\nList of users borrowed this book')
                for user in users_lst:
                    print(user.simple_repr())

    def print_users(self):
        users_str = '\n'.join([str(user) for user in self.backend.users])
        print(users_str)

if __name__ == '__main__':
    app = FrontendManager()
    app.run()
