# project library management system 

class Library:
  def __init__(self, name):
      self.name = name
      self.books = {}

  def add_book(self, book, quantity=1):
      if book in self.books:
          self.books[book] += quantity
      else:
          self.books[book] = quantity

  def display_books(self):
      print("Available Books:")
      for book, quantity in self.books.items():
          print(f"{book} - Quantity: {quantity}")

  def borrow_book(self, book):
      if book in self.books and self.books[book] > 0:
          self.books[book] -= 1
          print(f"You have borrowed {book}. Enjoy reading!")
      else:
          print(f"Sorry, {book} is not available for borrowing.")

  def return_book(self, book):
      if book in self.books:
          self.books[book] += 1
          print(f"Thank you for returning {book}.")
      else:
          print("This book is not part of our library.")


def main():
  library_name = input("Enter library name: ")
  library = Library(library_name)

  while True:
      print("\nLibrary Management System")
      print("1. Add a Book")
      print("2. Display Available Books")
      print("3. Borrow a Book")
      print("4. Return a Book")
      print("5. Quit")

      choice = input("Enter your choice: ")

      if choice == '1':
          book_name = input("Enter book name: ")
          quantity = int(input("Enter quantity: "))
          library.add_book(book_name, quantity)
          print(f"{quantity} copies of {book_name} added to the library.")

      elif choice == '2':
          library.display_books()

      elif choice == '3':
          book_name = input("Enter book name: ")
          library.borrow_book(book_name)

      elif choice == '4':
          book_name = input("Enter book name: ")
          library.return_book(book_name)

      elif choice == '5':
          print("Thank you for using the Library Management System. Goodbye!")
          break

      else:
          print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
  main()
