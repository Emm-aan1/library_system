from library_mgt import add_book, search_book, list_books, delete_book

def get_user_choice():
  """
  Presents the menu and returns the user's choice as an integer.
  """
  print("\nLibrary Management System")
  print("1. Add Book")
  print("2. Search Book")
  print("3. List Books")
  print("4. Delete Book")
  print("5. Exit")

  while True:
    try:
      choice = int(input("Enter your choice (1-5): "))
      if 1 <= choice <= 5:
        return choice
      else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  """
  Main function to run the program with user interaction.
  """
  while True:
    choice = get_user_choice()

    if choice == 1:
      title = input("Enter book title: ").strip().lower()
      author = input("Enter book author: ").strip().lower()
      ISBN = input("Enter book ISBN: ").strip().lower()
      add_book(title, author, ISBN)
    elif choice == 2:
      title = input("Enter book title to search: ").strip().lower()
      search_book(title)
      break;
    elif choice == 3:
      list_books()
    elif choice == 4:
      title = input("Enter book title to delete: ").strip().lower()
      delete_book(title)
      break;
    else:
      print("Exiting program...")
      break

if __name__ == "__main__":
  main()
