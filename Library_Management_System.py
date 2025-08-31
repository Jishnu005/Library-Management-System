from collections import defaultdict, deque

# Book Details
class Node:
    def __init__(self, book_id, book_name, author = None, left = None, right = None):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.left = left
        self.right = right

# Adding Books
def insert(node, book_id, book_name, author = None):
    if not node:
        return Node(book_id, book_name, author)
    
    if book_id < node.book_id:
        node.left = insert(node.left, book_id, book_name, author)

    elif book_id > node.book_id:
        node.right = insert(node.right, book_id, book_name, author)
    
    return node

def min_value_BST(node):
    current = node
    while current.left:
        current = current.left
    return current

# Remove Books
def removal(node, book_id):
    if not node:
        return node
    
    if book_id < node.book_id:
        node.left = removal(node.left, book_id)
    elif book_id > node.book_id:
        node.right = removal(node.right, book_id)

    else:
        if not node.right:
            return node.left
        elif not node.left:
            return node.right
        
        mini = min_value_BST(node.right)
        node.book_id = mini.book_id
        node.book_name = mini.book_name
        node.author = mini.author
        node.right = removal(node.right, mini.book_id)
    
    return node

# Searching a particular book by it's id'
def search_book(node, book_id):
    if not node:
        return None
    if node.book_id == book_id:
        return node
    if book_id < node.book_id:
        return search_book(node.left, book_id)
    else:
        return search_book(node.right, book_id)

        
# See all the Books and their Authors
class check_books:
    def check_book(self, node):
        print("Book ID|Book Name|Author")
        self.__check_all_books(node)

    def __check_all_books(self, node):
        if node:
            self.__check_all_books(node.left)
            print(f"{node.book_id}|{node.book_name}|{node.author}")
            self.__check_all_books(node.right)

#Borrowing Book
def borrow_book(node, borrow_name, book_id):
    if not borrow_list[book_id]:
        borrow_list[book_id].append(borrow_name)
        book_node = search_book(node, book_id)
        if book_node:
            print(borrow_name, "just borrowed:", book_node.book_name)
        else:
            print("Book not found.")

    
    else:
        print("Someone already borrowed this book. Please wait in waiting line.")
        print("Waiting line:", len(borrow_list[book_id]) - 1)
        borrow_list[book_id].append(borrow_name)

class check_availability:
    def __availability(self, node):
        if node:
            self.__availability(node.left)
            if not borrow_list[node.book_id]:
                print(f"{node.book_id}|{node.book_name}|{node.author}")
            self.__availability(node.right)
    
    def availability(self, node):
        print("Book ID|Book Name|Author")
        self.__availability(node)
    
def return_book(book_id):
    if borrow_list[book_id]:
        borrow_list[book_id].popleft()
        if borrow_list[book_id]:
            nextp = borrow_list[book_id]
            print("Now book is borrowed by:", nextp[0])

borrow_list = defaultdict(deque)
node = None

def menu():
    global node
    opt = int(input("""   Library Management System
--------------------------------
1. Add Book
2. Remove Book
3. Borrow Book
4. Return Book
5. Search Book by ID
6. Show Available Books
7. Show All Books
0. Exit
--------------------------------
  Enter your choice: """))
    
    if opt == 1:
        # Adding Book
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        node = insert(node, book_id, book_name, author)
        print("Book added successfully.")

    elif opt == 2:
        # Removing Book
        book_id = int(input("Enter Book ID to remove: "))
        node = removal(node, book_id)
        print("Book removed successfully.")

    elif opt == 3:
        # Borrow Book
        borrow_name = input("Enter your name: ")
        book_id = int(input("Enter Book ID to borrow: "))
        borrow_book(node, borrow_name, book_id)

    elif opt == 4:
        # Return Book
        book_id = int(input("Enter Book ID to return: "))
        return_book(book_id)

    elif opt == 5:
        # Search Book by ID
        book_id = int(input("Enter Book ID to search: "))
        result = search_book(node, book_id)
        if result:
            print(f"Found: {result.book_name} by {result.author}")
        else:
            print("Book not found.")
    
    elif opt == 6:
        # Check available books
        available = check_availability()
        available.availability(node)

    elif opt == 7:
        # See all Books
        checker = check_books()
        checker.check_book(node)

    elif opt == 0:
        print("Exiting the system. Goodbye!")

    else:
        print("Wrong Input...")

while True:
    menu()
    i = int(input("Want to Exit\nPress '1' for YES\nPress '2' for NO:"))
    if i != 2:
        break

