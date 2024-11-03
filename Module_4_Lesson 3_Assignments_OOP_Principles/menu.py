from budget_category import BudgetCategory
from database import initialize_database, add_category_to_db, update_category_in_db, get_category_from_db, get_all_categories_from_db

def show_menu():
    print("\nPersonal Budget Management Menu")
    print("1. Create New Budget Category")
    print("2. Add Expense to Category")
    print("3. Display Budget Category Summary")
    print("4. Show All Categories")
    print("5. Exit")