class Transaction:
    def __init__(self, date, action, amount):
        self.__date = date
        self.__action = action
        self.__amount = amount

    def display(self):
        print(self.__date + ": " + self.__action + " for " + self.__amount)