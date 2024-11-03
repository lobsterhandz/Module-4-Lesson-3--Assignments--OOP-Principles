import unittest
from budget_category import BudgetCategory

class TestBudgetCategory(unittest.TestCase):
    def setUp(self):
        self.food_category = BudgetCategory("Food", 500)

    def test_initial_budget(self):
        self.assertEqual(self.food_category.get_allocated_budget(), 500)
        self.assertEqual(self.food_category.get_category_name(), "Food")

    def test_set_category_name(self):
        self.food_category.set_category_name("Groceries")
        self.assertEqual(self.food_category.get_category_name(), "Groceries")

    def test_set_allocated_budget(self):
        self.food_category.set_allocated_budget(600)
        self.assertEqual(self.food_category.get_allocated_budget(), 600)

    def test_add_expense(self):
        self.food_category.add_expense(100)
        self.assertEqual(self.food_category._BudgetCategory__remaining_budget, 400)

    def test_add_expense_exceeds_budget(self):
        with self.assertRaises(ValueError):
            self.food_category.add_expense(600)

if __name__ == "__main__":
    unittest.main()
