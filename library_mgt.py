from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

# Get the database credentials
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

def connect_db():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error connecting to MySQL: ", e)
    return None

def close_db(connection):
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

def add_book(title, author, ISBN):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            check_query = "SELECT * FROM books WHERE title = %s OR author = %s OR ISBN = %s"
            val_query = (title, author, ISBN)
            cursor.execute(check_query, val_query)
            result = cursor.fetchone()

            if result:
                print("Book already exists")
            else:
                sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
                val = (title, author, ISBN)
                cursor.execute(sql, val)
                connection.commit()
                print("Book added successfully")
        except Error as e:
            print(f"Failed to add book: {e}")
        finally:
            cursor.close()
            close_db(connection)

def search_book(title):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            query_search = "SELECT * FROM books WHERE title LIKE %s"
            val = (f"%{title}%",)
            cursor.execute(query_search, val)
            results = cursor.fetchall()

            if results:
                for row in results:
                    print(f"Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
            else:
                print("No books found with the given title.")
        except Error as e:
            print(f"Book not found: {e}")
        finally:
            cursor.close()
            close_db(connection)

def list_books():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            query_list = "SELECT * FROM books"
            cursor.execute(query_list)
            results = cursor.fetchall()

            if results:
                for book in results:
                    print(f"The book title: {book[1]}, and the author: {book[2]}, with ISBN: {book[3]}.")
            else:
                print("No books found.")
        except Error as e:
            print(f"Failed to retrieve books: {e}")
        finally:
            cursor.close()
            close_db(connection)

def delete_book(title):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Search for books with titles that match the partial title
            query_search = "SELECT * FROM books WHERE title LIKE %s"
            val = (f"%{title}%",)
            cursor.execute(query_search, val)
            results = cursor.fetchall()

            if results:
                print("Matching books found:")
                for i, book in enumerate(results):
                    print(f"{i + 1}. Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")

                # Ask user to confirm which book to delete
                book_number = input("Enter the number of the book you want to delete: ")
                if book_number.isdigit():
                    book_selected = results[int(book_number) - 1]
                    query_delete = "DELETE FROM books WHERE id = %s"
                    val_delete = (book_selected[0],)
                    cursor.execute(query_delete, val_delete)
                    connection.commit()

                    print(f"Book '{book_selected[1]}' has been deleted")
                else:
                    print("Invalid selection. No book was deleted.")
            else:
                print("No books found with the given title.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            close_db(connection)

