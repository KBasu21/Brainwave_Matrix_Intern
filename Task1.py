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
        accounts = [["Dinesh Shenoy", "125423654587", "696", 500000.00], ["Roshan Misra", "456212307895", "123", 503.45], ["Madhur Tara", "123456789123", "602", 7853.15], ["Drishti Prakash", "541274588569", "452", 1375.00], ["Rashmi De", "564564213123",
                                                                                                                                                                                                                                 "874", 7854120.29], ["Devadas Borah", "951753456852", "999", 61542.99], ["Shivali Chowdhury", "741258963214", "543", 7894.22], ["Rudra Prabhakar", "875412985632", "666", 19485726.77], ["Tanvi Rajagopal", "545454545454", 545, 87954.21]]
        save_accounts(accounts)  # Save the initial data to CSV
    return accounts

# Save updated accounts to the CSV file


def save_accounts(accounts):
    with open("accounts.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        for account in accounts:
            # Write account data back to the CSV file, converting balance to string
            writer.writerow(account)


def find_account(card_number, accounts):
    # Find the account based on card number.
    for account in accounts:
        if account[1] == card_number:
            return account
    return None


def atm_interface():
    # ATM interface function.
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
                        print("4. Exit")
                        choice = input("Enter your choice: ")

                        if choice == '1':
                            # Deposit
                            amount = float(input("Enter amount to deposit: "))
                            account[3] += amount  # Update balance
                            print("Deposit successful! New balance: Rs.",
                                  account[3])
                            # Save updated account list to CSV
                            save_accounts(accounts)
                            print("Account information saved!")

                        elif choice == '2':
                            # Withdrawal
                            amount = float(input("Enter amount to withdraw: "))
                            if amount > account[3]:
                                print("Insufficient balance!")
                            else:
                                account[3] -= amount  # Update balance
                                print(
                                    "Withdrawal successful! New balance: Rs.", account[3])
                                # Save updated account list to CSV
                                save_accounts(accounts)
                                print("Account information saved!")

                        elif choice == '3':
                            # Check balance
                            print(f"Your current balance is: Rs.", account[3])

                        elif choice == '4':
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
