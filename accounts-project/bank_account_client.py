from accounts_database import Account, AccountsDatabase

def addAccount(accountsDb):
    accountType = input('Youth or Regular: ')
    accountNum = input('Enter account number: ')
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    startingBalance = input('Enter your starting balance: ')

    if not accountNum.isdigit():
        print('Invalid input. Please enter a numeric value for the account number.')
        return

    accountNum = int(accountNum)

    newAccount = Account(accountNum, firstName, lastName, startingBalance, accountType)

    accountsDb.addAccount(newAccount.accountNum, newAccount.firstName, newAccount.lastName, newAccount.startingBalance, newAccount.accountType)

    print('Account Details:')
    print(f'Account Holder: {newAccount.getFullName()}')
    print(f'Account Number: {newAccount.accountNum}')
    print(f'Account Type: {newAccount.accountType}')
    print(f'Starting Balance: {newAccount.startingBalance}')

def deleteAccount(accountsDb):
    accountNum = input('Enter account number: ')
    accountsDb.deleteAccount(accountNum)

def displayTotalAccounts(accountsDb):
    accountsDb.displayTotalAccounts()

def displayAllAccounts(accountsDb):
    accountsDb.displayAllAccounts()

def searchForAccount(accountsDb):
    accountNum = input('Enter account number: ')
    accountsDb.searchAccount(accountNum)

def exitProgram(accountsDb):
    with open('bankAccounts.txt', 'w') as file:
        for row in accountsDb.cur.execute('SELECT * FROM accounts'):
            file.write(str(row) + '\n')
# my tutor friend also helped with this part because after i edited my code, it wouldn't let me exit anymore like it used to
    print('Exiting...')
    print('Goodbye!')

def main():
    accountsDb = AccountsDatabase()

    while True:
        print('\nMenu:')
        print('1. Create customer bank account')
        print('2. Delete Account')
        print('3. Display all accounts')
        print('4. Display total number of accounts')
        print('5. Search for an account')
        print('6. Exit')

        option = input('Enter your choice (1-6): ')

        if option == '1':
            addAccount(accountsDb)
        elif option == '2':
            deleteAccount(accountsDb)
        elif option == '3':
            displayAllAccounts(accountsDb)
        elif option == '4':
            displayTotalAccounts(accountsDb)
        elif option == '5':
            searchForAccount(accountsDb)
        elif option == '6':
            exitProgram(accountsDb)
            break
        else:
            print('Invalid option. Please enter a number from 1 to 6.')

if __name__ == '__main__':
    main()
