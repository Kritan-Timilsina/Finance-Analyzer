import datetime as dt
transactions = []
id_counter = 1


def input_transaction(transactions):
    global id_counter
    try:
        input_date = dt.datetime.strptime(
            input("Enter the date of transaction(DD/MM/YYYY): "), '%d/%m/%Y')
    except ValueError:
        print("Invalid date format. Please enter date in DD/MM/YYYY format. ")
        return
    input_type = input(
        "Enter the type of transaction (income/expense): ").lower()
    if input_type not in ["income", "expense"]:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")
        return
    input_amount = float(input("Enter the amount: "))
    input_description = input("Enter a description for the transaction: ")

    for index, category in enumerate(income_categories if input_type == "income" else expense_categories):
        print(f"{index + 1}. {category}")

    input_category_index = int(input("Select a category: "))

    transaction = {
        "id": id_counter,
        "date": input_date,
        "type": input_type,
        "amount": input_amount,
        "description": input_description,
        "category": income_categories[input_category_index - 1] if input_type == "income" else expense_categories[input_category_index - 1]

    }
    transactions.append(transaction)
    id_counter += 1


def display_type_transactions(transactions, cat):
    if cat not in ["income", "expense"]:
        print("Invalid transaction type. Please enter 'income'or 'expense'. ")
        return
    elif cat == "income":
        filtered_transactions = [
            transaction for transaction in transactions if transaction['type'] == 'income']
        display_transactions(filtered_transactions)
    else:
        filtered_transactions = [
            transaction for transaction in transactions if transaction['type'] == 'expense']
        display_transactions(filtered_transactions)


def display_transactions(transactions):
    if not transactions:
        print("No transactions to display.")
        return

    else:
        print("Transactions: ")
        for transaction in transactions:
            print(
                f" id: {transaction['id']} \nDate: {transaction['date'].strftime('%d/%m/%y')}\n Type: {transaction['type']}\nAmount: {transaction['amount']}\nDescription: {transaction['description']} \nCategory: {transaction['category']}\n")


def delete_transactions(transactions, input_id):
    for transaction in transactions:
        if transaction['id'] == input_id:
            transactions.remove(transaction)
            print("ID Sucessfully Deleted ")

            break
    else:
        print("ID not found!!!")

def net_Cashflow(transactions):
   
    total_income=[transaction['amount']  for transaction in transactions if transaction['type']=='income']  
    total_expense= [transaction['amount'] for transaction in transactions if transaction['type'] == 'expense'] 
    total_cashflow= sum(total_income)-sum(total_expense)
    print(f"Total Cashflow: {total_cashflow}")
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
while True:
    print("Enter your choice: ")
    print("1. Add a transaction\n2. Display all transactions\n3. Delete a transaction\n4. Display by type(income/expense) \n5. Net Cashflow\n10. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            input_transaction(transactions)
        case "2":
            display_transactions(transactions)
        case "3":
            input_id = int(
                input("Enter the Id of the transaction you want to delete: "))
            delete_transactions(transactions, input_id)
        case "4":

            cat = input(
                "Enter the Type of transaction which you want to display: ").lower()
            display_type_transactions(transactions,cat)
        case "5": 
             net_Cashflow(transactions)

        case "10":
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again. ")

