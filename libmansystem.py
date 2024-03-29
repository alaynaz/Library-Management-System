

class Library:
    def __init__(self, file_path="books.txt"):

        self.file_path = file_path
        self.file = open(self.file_path, "a+")                                             #opens the books.txt file

    def __del__(self):
        self.file.close()                                                                  #closes the file

    def list_books(self):
        self.file.seek(0)                                                                  #moves to the beginning
        book_lines = self.file.read().splitlines()                                         #reads all lines from the file
        for line in book_lines:
            book_info = line.split(',')                                                    #splits the book informations with comma
            print(f"The book's title: {book_info[0]}, The book's author: {book_info[1]}")  #prints title and author's name

    def add_book(self):
        title = input("Book's title: ")
        author = input("Book's author: ")
        release_year = input("Book's release year: ")
        num_pages = input("Book's number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"                       #book's information
        self.file.write(book_info)                                                         #writes informations to the file
        print("Book is added successfully.")

    def remove_book(self):
        title_to_remove = input("What's the title of the book you want to remove: ")

        self.file.seek(0)                                                                  #moves to the beginning
        book_lines = self.file.read().splitlines()                                         #reads lines from the file
        matching_books = [line.split(',') for line in book_lines if line.startswith(title_to_remove + ',')]

        if len(matching_books) > 1:                                                        #if there are books that have the same title
            print(f"There are {len(matching_books)} books with the same title.")           #shows how many books that have the same title
            author_to_remove = input("What's the author of the book you want to remove: ")
            matching_books = [book for book in matching_books if book[1] == author_to_remove]  #removes the book after getting the author's name


            if not matching_books:
                print("Book is not found.")
                return

        if not matching_books:
            print("Book is not found.")
            return

        for book in matching_books:
            book_lines.remove(','.join(book))                                             #removes the book

        self.file.seek(0)                                                                 #moves to the beginning
        self.file.truncate()                                                              #clears the contents of the file
        self.file.writelines('\n'.join(book_lines))                                       #writes the updated book list to the file
        print("Book is removed successfully.")

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")

    choice = input("What's your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':                                                           #closes the program when q or Q is pressed
        print("Thank you for using my library management system. Goodbye")
        break
    else:
        print("Press one of those options: 1, 2, 3 or Q to quit")

