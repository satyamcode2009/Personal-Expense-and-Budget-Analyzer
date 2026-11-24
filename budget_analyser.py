import csv
import os
from datetime import datetime

# --- Activity 6: Object-Oriented Design (Encapsulation & Inheritance) ---
class Transaction:
    """Base class representing a general financial transaction."""
    def __init__(self, amount, category):
        self._amount = amount        # Protected attribute (Encapsulation)
        self._category = category
        self._date = datetime.now().strftime("%Y-%m-%d")

    def get_amount(self):
        return self._amount

    def get_category(self):
        return self._category

    def get_date(self):
        return self._date


class Expense(Transaction):
    """Child class inheriting from Transaction (Inheritance)."""
    def __init__(self, amount, category, note=""):
        super().__init__(amount, category)
        self.note = note

    def display(self):
        return f"{self._date} | {self._category:<12} | Rs. {self._amount:>8.2f} | {self.note}"


# --- Activity 3: Modular Class & Isolated Functions ---
class BudgetAnalyzer:
    def __init__(self, monthly_budget):
        self.__monthly_budget = monthly_budget  # Private attribute (Encapsulation)
        self.expenses = []

    def add_expense(self, amount, category, note=""):
        if amount <= 0:
            print("Invalid amount! Expense must be greater than 0.")
            return
        exp = Expense(amount, category, note)
        self.expenses.append(exp)
        self.save_to_csv(exp)
        print(f"Expense of Rs. {amount:.2f} added under '{category}'.")

    def save_to_csv(self, exp):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses_data.csv")
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([exp.get_date(), exp.get_category(), exp.get_amount(), exp.note])

    def view_summary(self):
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        print("\n--- Expense Summary ---")
        print(f"{'Date':<10} | {'Category':<12} | {'Amount':>12} | Note")
        print("-" * 55)
        total = 0
        for exp in self.expenses:
            print(exp.display())
            total += exp.get_amount()
        print("-" * 55)
        print(f"Total Expenditure: Rs. {total:.2f} / Rs. {self.__monthly_budget:.2f}")

    # --- Activity 5: Nested Conditions (Decision Tree Logic) ---
    def check_budget_alert(self):
        total = sum(exp.get_amount() for exp in self.expenses)
        remaining = self.__monthly_budget - total
        usage_percent = (total / self.__monthly_budget) * 100

        print(f"\nCurrent Total Expense: Rs. {total:.2f} ({usage_percent:.1f}% of budget)")
        if total > 0:
            if total > self.__monthly_budget:
                print("*** WARNING: Budget Limit Exceeded! ***")
                print(f"You are over budget by Rs. {abs(remaining):.2f}.")
            else:
                if usage_percent >= 80:
                    print("* ALERT: You have used 80% or more of your budget! *")
                    print(f"Remaining Budget: Rs. {remaining:.2f}. Spend carefully.")
                else:
                    print("SAFE: You are well within your budget.")
                    print(f"Remaining Budget: Rs. {remaining:.2f}")
        else:
            print("No expenses added yet. Full budget is available!")

    # --- Activity 7: Data Interpretation (Table, Chart & Insights) ---
    def data_insights(self):
        if not self.expenses:
            print("\nNo data available for analysis.")
            return

        category_totals = {}
        for exp in self.expenses:
            cat = exp.get_category()
            category_totals[cat] = category_totals.get(cat, 0) + exp.get_amount()

        total = sum(category_totals.values())
        avg_expense = total / len(self.expenses)
        highest_cat = max(category_totals, key=category_totals.get)

        print("\n--- Category-wise Data Analysis & Visual Chart ---")
        print(f"{'Category':<12} | {'Total (Rs.)':>11} | {'Share (%)':>9} | Visual Bar")
        print("-" * 60)
        for cat, amt in category_totals.items():
            pct = (amt / total) * 100
            bar = "#" * int(pct // 5)
            print(f"{cat:<12} | {amt:>11.2f} | {pct:>8.1f}% | {bar}")

        print("\n--- Key Insights ---")
        print(f"1. Highest Spending Category : {highest_cat} (Rs. {category_totals[highest_cat]:.2f})")
        print(f"2. Average Expense per Entry : Rs. {avg_expense:.2f}")
        print(f"3. Total Transactions        : {len(self.expenses)}")


def main():
    print("=== Personal Expense & Budget Analyzer (Milestone 2) ===")
    while True:
        try:
            budget = float(input("Enter your monthly pocket money budget (e.g., 5000): "))
            if budget <= 0:
                print("Please enter a positive budget amount.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    analyzer = BudgetAnalyzer(budget)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Check Budget Alert")
        print("4. Data Analysis & Insights")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter category (e.g., Canteen, Travel, Shopping): ").strip()
                note = input("Enter short note (optional): ").strip()
                analyzer.add_expense(amount, category, note)
            except ValueError:
                print("Invalid input! Please enter a number for amount.")
        elif choice == '2':
            analyzer.view_summary()
        elif choice == '3':
            analyzer.check_budget_alert()
        elif choice == '4':
            analyzer.data_insights()
        elif choice == '5':
            print("Data saved to expenses_data.csv. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()