import mysql.connector as c

conn = c.connect(host="localhost", user="root", passwd="mysql", database="bankaccounts")
cursor = conn.cursor()

print("===== Welcome to bank management system =====")
while True:

    print("\nChoose any one option:")
    print("Press 1 --> Open zero balance bank account")
    print("Press 2 --> Deposit cash in bank account")
    print("Press 3 --> Withdraw cash from bank account")
    print("Press 4 --> Display bank account details")
    print("Press 5 --> Close the bank account")
    print("Press 6 --> EXIT")
    option = int(input("Enter option > "))

    if option == 1:
        accno = input("Enter account number > ")
        name = input("Enter name of account holder > ")
        date = input("Enter date of opening in DD/MM/YYYY format > ")
        query1 = "INSERT INTO accounts VALUES ('{}', '{}', '{}', {})".format(accno, name, date, 0)
        cursor.execute(query1)
        conn.commit()
        print("Account created successfully!!")

    elif option == 2:
        accholder = input("Enter name whose account is to be updated > ")
        deposit = float(input("Enter amount to deposit > "))
        getbalanceQuery = "SELECT balance FROM accounts WHERE name = '{}'".format(accholder)
        cursor.execute(getbalanceQuery)
        balance = list(cursor.fetchone()).pop()
        query2 = "UPDATE accounts SET balance = {} WHERE name = '{}'".format(deposit + balance, accholder)
        cursor.execute(query2)
        conn.commit()

    elif option == 3:
        accholder = input("Enter account holder name > ")
        withdraw = float(input("Enter amount to withdraw > "))
        getbalanceQuery = "SELECT balance FROM accounts WHERE name = '{}'".format(accholder)
        cursor.execute(getbalanceQuery)
        balance = list(cursor.fetchone()).pop()

        if balance < withdraw:
            print("Not enough balance!!")
        else:
            query3 = "UPDATE accounts SET balance = {} WHERE name = '{}'".format(balance - withdraw, accholder)
            cursor.execute(query3)
            conn.commit()

    elif option == 4:
        accholder = input("Enter name of account holder > ")
        query4 = "SELECT * FROM accounts WHERE name = '{}'".format(accholder)
        cursor.execute(query4)
        print("\n")
        result = cursor.fetchone()
        if result is None:
            print("Bank account not found!!!")
        else:
            print("+----------------------------------------------------------+")
            print("|  Acc no.   |   Name   |   Date Of Opening   |   Balance  |")
            print("+----------------------------------------------------------+")
            print(result)

    elif option == 5:
        accholder = input("Enter name account holder whose account is to be closed > ")
        query5 = "DELETE FROM accounts WHERE name = '{}'".format(accholder)
        cursor.execute(query5)
        conn.commit()

    elif option == 6:
        break

    else:
        print("Invalid option")

print("===== Thank you!! =====")
