import pandas as pd
import matplotlib.pyplot as plt

class PersonalFinanceTracker:
    def _init_(self):
        # Initialize an empty DataFrame with specified columns
        self.transactions = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])

    def add_transaction(self, date, category, amount, t_type):
        """
        Add a transaction (Income or Expense).
        :param date: Transaction date
        :param category: Category of the transaction
        :param amount: Amount in the transaction
        :param t_type: Type - 'Income' or 'Expense'
        """
        new_transaction = {"Date": date, "Category": category, "Amount": amount, "Type": t_type}
        # Add the new transaction to the DataFrame
        self.transactions = pd.concat([self.transactions, pd.DataFrame([new_transaction])], ignore_index=True)

    def view_summary(self):
        """Display income, expenses, and savings summary."""
        income = self.transactions[self.transactions["Type"] == "Income"]["Amount"].sum()
        expenses = self.transactions[self.transactions["Type"] == "Expense"]["Amount"].sum()
        savings = income - expenses

        print("\n--- Financial Summary ---")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Savings: ${savings:.2f}\n")

    def visualize_expenses(self):
        """Display a pie chart of expenses by category."""
        expense_data = self.transactions[self.transactions["Type"] == "Expense"]
        if expense_data.empty:
            print("No expenses to visualize!")
            return

        # Group expenses by category and plot a pie chart
        category_totals = expense_data.groupby("Category")["Amount"].sum()
        category_totals.plot.pie(autopct="%1.1f%%", figsize=(8, 8))
        plt.title("Expenses by Category")
        plt.ylabel("")  # Hide y-axis label
        plt.show()

    def export_to_csv(self, filename="finance_data.csv"):
        """Export the transactions to a CSV file."""
        self.transactions.to_csv(filename, index=False)
        print(f"Data exported to {filename}")

# Main Program
if _name_ == "_main_":  # Corrected if condition for main block
    tracker = PersonalFinanceTracker()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Visualize Expenses")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter income source: ")
            amount = float(input("Enter amount: "))
            tracker.add_transaction(date, category, amount, "Income")

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            tracker.add_transaction(date, category, amount, "Expense")

        elif choice == "3":
            tracker.view_summary()

        elif choice == "4":
            tracker.visualize_expenses()

        elif choice == "5":
            filename = input("Enter filename (default: finance_data.csv): ") or "finance_data.csv"
            tracker.export_to_csv(filename)

        elif choice == "6":
            print("Exiting... Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")