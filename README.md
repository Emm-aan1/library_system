# Library Management System

This Python project is a simple library management system that interacts with a MySQL database to perform operations on a collection of books. The system provides functionality to add, search, list, and delete books from the database.

## Features

- **Add Book:** Add new books to the library.
- **Search Book:** Search for books based on title.
- **List Books:** List all books in the library.
- **Delete Book:** Delete books from the library based on user input.

## Setup

### Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library
- `python-dotenv` library

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Emm-aan1/library_management.git
    cd library-management
    ```

2. **Install the required Python packages:**

    ```bash
    pip install mysql-connector-python python-dotenv
    ```

3. **Set up your `.env` file:**

    Create a `.env` file in the root directory of the project with the following content:

    ```plaintext
    DB_HOST=your_database_host
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name
    ```

    Replace `your_database_host`, `your_database_user`, `your_database_password`, and `your_database_name` with your MySQL server credentials.

4. **Create the database and `books` table:**

    Run the following SQL commands in your MySQL server to create the database and the `books` table:

    ```sql
    CREATE DATABASE your_database_name;

    USE your_database_name;

    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        ISBN VARCHAR(20) NOT NULL
    );
    ```

## Usage

### Add a Book

To add a book to the library:

```python
add_book(title, author, ISBN)
```

### Search for Books

To search for books by title:

```python
search_book(title)
```

### List All Books

To list all books in the library:

```python
list_books()
```

### Delete a Book

To delete a book based on its title:

```python
delete_book(title)
```

## Code Overview

- **`connect_db`**: Connects to the MySQL database using credentials from the `.env` file.
- **`close_db`**: Closes the database connection.
- **`add_book`**: Adds a new book to the `books` table if it does not already exist.
- **`search_book`**: Searches for books by partial title and displays matching results.
- **`list_books`**: Lists all books in the `books` table.
- **`delete_book`**: Deletes a book based on user input and confirms the deletion.

## License

This project does not have a specific license. Feel free to use or modify the code as needed.


