# README.md

# Personal Budget Management Application

This repository contains a simple personal budget management application built with Python. The program allows users to manage their expenses across different budget categories. The project uses SQLite for secure data storage and follows a modular design for better maintainability and scalability.

## Features
- **Create a New Budget Category**: Allows users to create a new budget category, specifying a budget allocation.
- **Add Expense to Category**: Users can add expenses to a specific category, which deducts from the remaining budget.
- **Display Budget Category Summary**: Shows the details of a specific budget category, including the category name, allocated budget, and remaining budget.
- **Show All Categories**: Displays all budget categories and their corresponding allocated and remaining budgets.
- **Data Persistence**: All budget categories and related data are stored securely using SQLite, ensuring data persistence.

## Project Structure
```
.
├── budget_category.py        # Contains the BudgetCategory class definition
├── database.py               # Contains functions for interacting with the SQLite database
├── menu.py                   # Menu-driven interface to interact with the budget management system
├── test_budget_category.py   # Unit tests for the BudgetCategory class
└── budget.db                 # SQLite database (created automatically when the program is run)
```

## Getting Started

### Prerequisites
- Python 3.x

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure Python is installed on your system.

### Running the Program
- Run the program using the command:
  ```sh
  python menu.py
  ```
- Follow the menu prompts to create categories, add expenses, and view summaries.

## Usage
- **Create a New Budget Category**: When prompted, enter the category name and the allocated budget. This creates a new budget category stored in the SQLite database.
- **Add Expense to a Category**: Select this option to add an expense to an existing category. The expense is deducted from the remaining budget.
- **Display Category Summary**: Displays detailed information about a specific budget category.
- **Show All Categories**: Lists all existing categories along with their budgets.

## Example
```
Personal Budget Management Menu
1. Create New Budget Category
2. Add Expense to Category
3. Display Budget Category Summary
4. Show All Categories
5. Exit
Enter your choice (1-5): 1
Enter the category name: Food
Enter the allocated budget: 500
Alright, got it! The budget category 'Food' has been successfully created with $500.00 allocated.
```

## Testing
The project includes unit tests for the `BudgetCategory` class to ensure proper functionality. To run the tests, execute:
```sh
python test_budget_category.py
```

## Modules Overview

### 1. `budget_category.py`
This module defines the `BudgetCategory` class, which encapsulates budget details like the category name, allocated budget, and remaining budget. It provides methods to:
- Add expenses to a category.
- Get and set budget details.

### 2. `database.py`
This module contains functions to interact with the SQLite database:
- **`initialize_database`**: Creates the database and `budget_category` table if they don't exist.
- **`add_category_to_db`**: Adds a new category to the database.
- **`update_category_in_db`**: Updates the remaining budget for a specific category.
- **`get_category_from_db`**: Fetches a category's details.
- **`get_all_categories_from_db`**: Fetches all budget categories from the database.

### 3. `menu.py`
This module provides a menu-driven interface to interact with the user, allowing them to create categories, add expenses, display specific category summaries, and view all categories.

### 4. `test_budget_category.py`
This module provides unit tests for the `BudgetCategory` class to ensure that the functionalities work as expected, including validation of setting budgets, adding expenses, and handling edge cases like overspending.

## Exception Handling
- The application includes exception handling to ensure that only valid inputs are processed.
- **Database errors**: Errors during database operations are caught and displayed to prevent crashes.
- **Value errors**: Input validation for budget and expense amounts ensures only positive numbers are used.

## Future Improvements
- Add user authentication for accessing the budget management system.
- Implement advanced analytics to visualize spending trends.
- Integrate a graphical user interface (GUI) for better user experience.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes you would like to make.

## Author
- **Jose** - Main developer of this personal budget management application.
