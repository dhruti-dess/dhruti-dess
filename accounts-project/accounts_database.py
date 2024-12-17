import sqlite3

class Account:
    def __init__(self, accountNum, firstName, lastName, startingBalance, accountType):
        self.accountNum = accountNum
        self.firstName = firstName
        self.lastName = lastName
        self.startingBalance = startingBalance
        self.accountType = accountType

    def getFullName(self):
        return (f'{self.firstName} {self.lastName}')
    
class AccountsDatabase:
    def __init__(self, database='accountDb'):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute('CREATE TABLE if not exists accounts(accountNum INTEGER, firstName VARCHAR(20), lastName VARCHAR(20), startingBalance REAL, accountType VARCHAR(20))')
        self.conn.commit()

    def addAccount(self, accountNum, firstName, lastName, startingBalance, accountType):
        self.cur.execute('INSERT INTO accounts VALUES (?, ?, ?, ?, ?)', (accountNum, firstName, lastName, startingBalance, accountType))
        self.conn.commit()

    def deleteAccount(self, accountNum):
        self.cur.execute('DELETE FROM accounts WHERE accountNum=?', (accountNum,))
        self.conn.commit()

    def searchAccount(self, accountNum):
        for row in self.cur.execute('SELECT * FROM accounts WHERE accountNum=?', (accountNum,)):
            print(row)

    def displayTotalAccounts(accountsDb):
        accountsDb.cur.execute('SELECT COUNT(*) FROM accounts')
        totalAccounts = accountsDb.cur.fetchone()[0] # I did not know how to get the total number so I asked my friend who is a tutor to help, sorry if it is not part of the class material, I struggled a lot
        print("Total accounts:", totalAccounts)


    def displayAllAccounts(self):
        for row in self.cur.execute('SELECT accountNum, firstName, lastName, accountType, startingBalance FROM accounts'):
            print(row)

    def disconnect(self):
        self.conn.close()



