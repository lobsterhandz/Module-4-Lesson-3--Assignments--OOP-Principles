
from budget_category import BudgetCategory
from menu import show_menu
from database import initialize_database, add_category_to_db, update_category_in_db, get_category_from_db, get_all_categories_from_db

if __name__ == "__main__":
    initialize_database()
    categories = {}
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            category_name = input("Enter the category name: ")
            try:
                allocated_budget = float(input("Enter the allocated budget: "))
                categories[category_name] = BudgetCategory(category_name, allocated_budget)
                add_category_to_db(category_name, allocated_budget, allocated_budget)
                print(f"Alright, got it! The budget category '{category_name}' has been successfully created with ${allocated_budget:.2f} allocated.")
            except ValueError:
                print("Whoops! That's not a valid budget amount. Make sure to enter a number.")
            except Exception as e:
                print(f"Unexpected error occurred: {e}")

        elif choice == "2":
            category_name = input("Enter the category name to add an expense: ")
            if category_name in categories:
                try:
                    expense_amount = float(input("Enter the expense amount: "))
                    categories[category_name].add_expense(expense_amount)
                    update_category_in_db(category_name, categories[category_name]._BudgetCategory__remaining_budget)
                    print(f"Nice! An expense of ${expense_amount:.2f} has been added to '{category_name}'. Keep on track!")
                except ValueError as e:
                    print(f"Error: {e}. Please try again with a valid amount.")
                except Exception as e:
                    print(f"Something went sideways: {e}")
            else:
                print(f"Hmm, looks like '{category_name}' isn't on the list. Maybe create it first?")

        elif choice == "3":
            category_name = input("Enter the category name to display summary: ")
            category_data = get_category_from_db(category_name)
            if category_data:
                print(f"Category: {category_data[0]}")
                print(f"Allocated Budget: ${category_data[1]:.2f}")
                print(f"Remaining Budget: ${category_data[2]:.2f}")
            else:
                print(f"Category '{category_name}' doesn't exist. Are you sure you spelled it right?")

        elif choice == "4":
            all_categories = get_all_categories_from_db()
            if all_categories:
                print("\nAll Budget Categories:")
                for category in all_categories:
                    print(f"Category: {category[0]}, Allocated Budget: ${category[1]:.2f}, Remaining Budget: ${category[2]:.2f}")
            else:
                print("No categories found in the database.")

        elif choice == "5":
            print("Alright, exiting Personal Budget Management. Take care and stay on top of your expenses!")
            break

        else:
            print("Invalid choice. Come on, it's gotta be a number between 1 and 5.")