import sqlite3

# Task 1: Define Budget Category Class
# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.
class BudgetCategory:
    def __init__(self, category_name: str, allocated_budget: float):
        # Private attributes to ensure encapsulation
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Task 2: Implement Getters and Setters
    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name (with optional validation if necessary)
    def set_category_name(self, name: str):
        if isinstance(name, str) and len(name) > 0:
            self.__category_name = name
        else:
            raise ValueError("Category name must be a non-empty string.")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget (with validation to ensure it is a positive value)
    def set_allocated_budget(self, budget: float):
        if budget >= 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  # Reset remaining budget to match the new allocated budget
        else:
            raise ValueError("Budget must be a positive number.")

    # Task 3: Add Budget Functionality
    # Method to add expenses to the category
    def add_expense(self, amount: float):
        if amount < 0:
            raise ValueError("Expense amount must be a positive number.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds the remaining budget.")
        self.__remaining_budget -= amount

    # Task 4: Display Budget Details
    # Method to display the category summary, including name, allocated, and remaining budget
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
