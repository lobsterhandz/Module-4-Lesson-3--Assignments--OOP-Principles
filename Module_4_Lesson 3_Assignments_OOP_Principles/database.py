import sqlite3

def initialize_database():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget_category (
                        category_name TEXT PRIMARY KEY,
                        allocated_budget REAL,
                        remaining_budget REAL)''')
    conn.commit()
    conn.close()

def add_category_to_db(category_name, allocated_budget, remaining_budget):
    try:
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO budget_category (category_name, allocated_budget, remaining_budget)
                          VALUES (?, ?, ?)''', (category_name, allocated_budget, remaining_budget))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Category '{category_name}' already exists in the database.")
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_category_in_db(category_name, remaining_budget):
    try:
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE budget_category SET remaining_budget = ? WHERE category_name = ?''',
                       (remaining_budget, category_name))
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def get_category_from_db(category_name):
    try:
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM budget_category WHERE category_name = ?''', (category_name,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def get_all_categories_from_db():
    try:
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM budget_category''')
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()