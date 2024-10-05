import csv

# Load accounts from the CSV file
def load_accounts():
    accounts = []
    try:
        with open("accounts.csv", mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Convert balance to a float value
                row[3] = float(row[3])
                accounts.append(row)
    except FileNotFoundError:
        # If the file doesn't exist, create an initial list of accounts
        accounts = [["Dinesh Shenoy", "125423654587", "696", 500000.00], ["Roshan Misra", "456212307895", "123", 503.45], ["Madhur Tara", "123456789123", "602", 7853.15], ["Drishti Prakash", "541274588569", "452", 1375.00], ["Rashmi De", "564564213123","874", 7854120.29], ["Devadas Borah", "951753456852", "999", 61542.99], ["Shivali Chowdhury", "741258963214", "543", 7894.22], ["Rudra Prabhakar", "875412985632", "666", 19485726.77], ["Tanvi Rajagopal", "545454545454", "545", 87954.21]]
        save_accounts(accounts)  # Save the initial data to CSV
    return accounts

# Save updated accounts to the CSV file
def save_accounts(accounts):
    with open("accounts.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        for account in accounts:
            writer.writerow(account)

def find_account(card_number, accounts):
    # Find the account based on card number.
    for account in accounts:
        if account[1] == card_number:
            return account
    return None

def ask_receipt():
    receipt_choice = input("Would you like a receipt for this transaction? (yes/no): ").lower()
    if receipt_choice == 'yes':
        print("Generating receipt...")
        return True
    return False

def print_receipt(transaction_type, amount, balance, account):
    print("\n=== Transaction Receipt ===")
    print(f"Account Holder: {account[0]}")
    print(f"Transaction Type: {transaction_type}")
    print(f"Amount: Rs. {amount}")
    print(f"New Balance: Rs. {balance}")
    print("==========================\n")

def change_pin(account):
    print("To change your PIN, we need to verify your current PIN.")
    while True:
        old_pin = input("Enter your current PIN: ")
        if old_pin == account[2]:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                account[2] = new_pin
                print("PIN changed successfully!")
                return
            else:
                print("PIN confirmation does not match, try again.")
        else:
            print("Wrong current PIN, try again!")

def transfer_money(account, accounts):
    recipient_card = input("Enter recipient's card number: ")
    recipient_account = find_account(recipient_card, accounts)
    if recipient_account:
        amount = float(input("Enter amount to transfer: "))
        if amount > account[3]:
            print("Insufficient balance!")
        else:
            account[3] -= amount  # Deduct amount from sender
            recipient_account[3] += amount  # Add amount to recipient
            print(f"Transfer successful! Rs. {amount} has been sent to {recipient_account[0]}.")
            save_accounts(accounts)  # Save updated account list to CSV
            if ask_receipt():
                print_receipt("Transfer", amount, account[3], account)
    else:
        print("Recipient account not found!")

def atm_interface():
    accounts = load_accounts()  # Load accounts from the CSV file at the start

    while True:
        # Input card number
        card_number = input("Please enter your card number: ")

        # Validate card number
        account = find_account(card_number, accounts)
        if account:
            while True:
                # Input and validate PIN
                pin = input("Please enter your PIN: ")
                if pin == account[2]:
                    print("Welcome,", account[0], "!")

                    # Display options after correct PIN
                    while True:
                        print("Please choose an option:")
                        print("1. Deposit")
                        print("2. Withdrawal")
                        print("3. Check Balance")
                        print("4. Transfer Money")
                        print("5. Change PIN")
                        print("6. Exit")
                        choice = input("Enter your choice: ")

                        if choice == '1':
                            # Deposit
                            amount = float(input("Enter amount to deposit: "))
                            account[3] += amount  # Update balance
                            print("Deposit successful! New balance: Rs.", account[3])
                            save_accounts(accounts)  # Save updated account list to CSV
                            if ask_receipt():
                                print_receipt("Deposit", amount, account[3], account)

                        elif choice == '2':
                            # Withdrawal
                            amount = float(input("Enter amount to withdraw: "))
                            if amount > account[3]:
                                print("Insufficient balance!")
                            else:
                                account[3] -= amount  # Update balance
                                print("Withdrawal successful! New balance: Rs.", account[3])
                                save_accounts(accounts)  # Save updated account list to CSV
                                if ask_receipt():
                                    print_receipt("Withdrawal", amount, account[3], account)

                        elif choice == '3':
                            # Check balance
                            print(f"Your current balance is: Rs.", account[3])

                        elif choice == '4':
                            # Transfer money
                            transfer_money(account, accounts)

                        elif choice == '5':
                            # Change PIN
                            change_pin(account)
                            save_accounts(accounts)  # Save updated PIN to CSV

                        elif choice == '6':
                            # Exit
                            print("Thank you for using the ATM. Goodbye!")
                            return

                        else:
                            print("Invalid option. Please try again.")

                else:
                    print("Wrong PIN, try again!")
        else:
            print("Couldn't find the account, please try again!")


# Start the ATM interface
atm_interface()
