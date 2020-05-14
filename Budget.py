import datetime

from Transaction import Transaction


class Budget:
    def __init__(self, name, startingAmount):
        self.__name = name
        self.__startingAmount = startingAmount
        self.__currentAmount = startingAmount
        self.__transactionsList = []
        self.__budgetPeriod = datetime.datetime.now().strftime("%m-%Y")

    def getName(self):
        return self.__name

    def getStartingAmount(self):
        return self.__startingAmount

    def getCurrentAmount(self):
        return self.__currentAmount

    def getBudgetPeriod(self):
        return self.__budgetPeriod

    def setName(self, name):
        self.__name = name

    def setStartingAmount(self, startingAmount):
        self.__startingAmount = startingAmount

    def displayTransactionsList(self):
        for i in self.__transactionsList:
            i.display()

    # This method updates current amount upon a transaction, creates a Transaction object, and adds the transaction
    # to the transaction list
    def updateCurrentAmount(self, action, amount):
        self.__currentAmount = round(self.__currentAmount + amount, 2)
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        transaction = Transaction(date, action, amount)
        self.__transactionsList.append(transaction)

    # This method checks if the current budget cycle is over by checking the date
    # return true if it is over, false otherwise
    def cycleOver(self):
        if datetime.datetime.now().strftime("%m-%Y") != self.__budgetPeriod:
            return True
        else:
            return False