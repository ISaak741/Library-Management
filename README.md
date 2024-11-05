# Library Management Module for Odoo

## Overview

This Odoo module provides a basic framework for managing a library. It streamlines library operations and offers functionalities for:

- **Student Management**: Create and manage student profiles.
- **Book Management**: Add, edit, and delete books, tracking titles, authors, genres, and quantity.
- **Book Borrowing & Returning**:
  - Track borrowed books, including borrowing students, borrow dates, and expected return dates.
  - Define borrowing limits based on student study level or other criteria.
  - Calculate fines for overdue books.
  - Automatically update book availability based on borrowings and returns.

## Installation

### Clone the Repository:

git clone https://github.com/ISaak741/Library-Management

### Install Dependencies:
- Ensure you have the necessary Odoo dependencies installed.

### Copy the Module:
- Copy the library_management directory to your Odoo addons path.

### Update Odoo's Database:
- Update your Odoo database to install the module.

## Usage
### Configure the Module:
- Customize module settings as needed, such as defining borrowing limits and fine rates.

### Create Books:
Add books to the library, specifying details like title, author, and quantity.

### Manage Students:
Create student profiles, including their study level and other relevant information.

### Borrowing & Returning Books:
- Students can borrow books within their limits.
- The system automatically tracks borrow dates and expected return dates.
- Students can return borrowed books, updating book availability.
- Track Overdue Books:
- The system calculates fines for overdue books based on defined late fees.

## Customization
You can customize the module to fit your specific library needs by:

- Adding more fields to the books and borrowed_books models.
- Implementing complex workflows for book borrowing and returning.
- Integrating the module with other Odoo modules, such as accounting or inventory.
