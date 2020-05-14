import datetime
import pickle

from Budget import Budget

prevBudgetCycles = {}

# Either loading a saved budget or creating a new budget
while True:
    choice = input("Please select an option:\n1. Load a saved budget\n2. Create a new budget\n")
    if choice == "1":
        file = input("Enter the name of your saved budget: ")
        file += ".dat"
        try:
            with open(file, 'rb') as f:
                currentBudget, prevBudgetCycles = pickle.load(f)
            break

        except FileNotFoundError:
            print("That file does not exist!")

    elif choice == "2":
        name = input("Enter a name for your new budget: ")
        startingAmount = input("Enter the max amount of money you want to spend each month: ")
        currentBudget = Budget(name, float(startingAmount))
        date = datetime.datetime.now().strftime("%m-%Y")
        print("Your budget for " + date + " is now created.")
        break
    else:
        print("Invalid choice.")

# Here, the user is performing as many actions as they would like, until they decide to exit
while True:
    if currentBudget.cycleOver():
        prevBudgetCycles[currentBudget.getBudgetPeriod()] = currentBudget
        currentBudget = Budget(currentBudget.getName(), currentBudget.getStartingAmount())

    choice = input("Please select an option:\n1. Document a transaction\n2. Check current amount of money available\n3."
                   " Change the max amount of money you want to spend each month\n4. Display the transactions made "
                   "during this budget cycle\n5. View a previous budget cycle\n6. Save your budget and exit the "
                   "program\n")
    if choice == "1":
        action = input("Enter what the transaction was for: ")
        amount = input("Enter the amount the transaction was for (make negative if it was a purchase): ")
        currentBudget.updateCurrentAmount(action, float(amount))

    elif choice == "2":
        print(currentBudget.getCurrentAmount())

    elif choice == "3":
        amount = input("Enter a new max amount of money you want to spend each month: ")
        currentBudget.setStartingAmount(float(amount))

    elif choice == "4":
        currentBudget.displayTransactionsList()

    elif choice == "5":
        print("Here are all the previous budget cycles:")
        for i in prevBudgetCycles:
            print(i)
        while True:
            cycle = input("Enter a previous budget cycle to view, or -1 to exit to main menu: ")
            try:
                if cycle == "-1":
                    break

                cycle = prevBudgetCycles[cycle]
                print("Final balance for this cycle: " + cycle.getCurrentAmount() + "\nTransactions made: " +
                      cycle.displayTransactionsList())

            except KeyError:
                print("That budget cycle does not exist.")

    elif choice == "6":
        file = currentBudget.getName()
        file += ".dat"
        with open(file, 'wb') as f:
            pickle.dump([currentBudget, prevBudgetCycles], f, protocol=2)
        break

    else:
        print("Invalid choice.")
