transactions = []
income_categories = [
    "Salary",
    "Business",
    "Investment",
    "Gift",
    "Other"
]

expense_categories = [
    "Food",
    "Transport",
    "Shopping",
    "Education",
    "Entertainment",
    "Bills",
    "Other"
]
print("Welcome to the Transaction Trackr!")
print("Please Enter your Transactions below. Type 'done' when you are finished.")

# Taking imput
input_date = input("Enter the date of transaction(DD/MM/YYYY): ")
input_amount = float(input("Enter the amount: "))
input_description = input("Enter a description for the transaction: ")
input_type = input("Enter the type of transaction (income/expense): ")
for index, category in enumerate(income_categories if input_type == "income" else expense_categories):
    print(f"{index + 1}. {category}")

input_category_index = int(input("Select a category: "))


transaction = {
    "date": input_date,
    "type": input_type,
    "amount": input_amount,
    "description": input_description,
    "category": income_categories[input_category_index - 1] if input_type == "income" else expense_categories[input_category_index - 1]

}
transactions.append(transaction)
print(transactions[0])
