import csv
from datetime import datetime, timedelta
from uuid import uuid4

class LibraryManagementSystem:
    def __init__(self):
        self.books_file = "books.csv"
        self.members_file = "members.csv"
        self.assignments_file = "assignments.csv"

    # Book Management
    def add_book(self, title, author, quantity):
        book_id = uuid4().hex
        with open(self.books_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([book_id, title, author, quantity])
        print(f"Book '{title}' added successfully.")

    def list_books(self):
        with open(self.books_file, mode='r') as file:
            reader = csv.reader(file)
            print("Available Books:")
            for row in reader:
                print(row)

    # Member Management
    def add_member(self, name, contact):
        member_id = uuid4().hex
        with open(self.members_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([member_id, name, contact])
        print(f"Member '{name}' added successfully.")

    def list_members(self):
        with open(self.members_file, mode='r') as file:
            reader = csv.reader(file)
            print("Registered Members:")
            for row in reader:
                print(row)

    # Book Assignment
    def assign_book(self, member_id, book_id):
        assignment_id = uuid4().hex
        # Check book availability
        books = []
        book_found = False
        with open(self.books_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == book_id and int(row[3]) > 0:
                    book_found = True
                    row[3] = str(int(row[3]) - 1)  # Decrement quantity
                books.append(row)

        if not book_found:
            print("Book not available or does not exist.")
            return

        # Update books file
        with open(self.books_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)

        # Add to assignments
        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=14)
        with open(self.assignments_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([assignment_id, member_id, book_id, issue_date.strftime('%Y-%m-%d'), due_date.strftime('%Y-%m-%d'), 'No'])
        print(f"Book ID '{book_id}' assigned to Member ID '{member_id}'.")

    def list_assignments(self):
        with open(self.assignments_file, mode='r') as file:
            reader = csv.reader(file)
            print("Book Assignments:")
            for row in reader:
                print(row)

# Example Usage
if __name__ == "__main__":
    library = LibraryManagementSystem()

    while True:
        print("\nLibrary Management System")
        print("1. List All Books")
        print("2. Add a Book")
        print("3. List All Members")
        print("4. Add a Member")
        print("5. Assign a Book")
        print("6. List All Assignments")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid Input. Please try again.")
            continue

        match choice:
            case 1:
                library.list_books()
            case 2:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                quantity = int(input("Enter the quantity of the book: "))
                library.add_book(title, author, quantity)
            case 3:
                library.list_members()
            case 4:
                name = input("Enter the name of the member: ")
                contact = input("Enter the contact of the member: ")
                library.add_member(name, contact)
            case 5:
                member_id = input("Enter the Member ID: ")
                book_id = input("Enter the Book ID: ")
                library.assign_book(member_id, book_id)
            case 6:
                library.list_assignments()
            case 7:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select from 1-7.")
