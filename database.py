import mysql.connector as c


# ==== creating a SQL class ====
class SQL:
    def __init__(self):
        """
        Constructor of `SQL` class
        """

        # to establish a connection
        self.con = c.connect(host='localhost', user='root', passwd='mysql', database='mysql')

        # making a cursor for the database
        self.cursor = self.con.cursor()

        table_create = "CREATE TABLE IF NOT EXISTS students(" \
                       "name VARCHAR(20)," \
                       "age INTEGER," \
                       "marks INTEGER)"
        self.cursor.execute(table_create)
        self.con.commit()

        # checking the connection is established or not
        # if con.is_connected():
        #     print("Connected successfully!!")

    def insert_data(self):
        """
        inserts data into existing table of the database

        :return: None
        """

        name = input("Enter your name > ")
        age = int(input("Enter your age > "))
        marks = float(input("Enter your marks > "))

        # inserting data using mysql commands
        query1 = "INSERT INTO students VALUES ('{}', {}, {})".format(name, age, marks)
        self.cursor.execute(query1)
        self.con.commit()

        print("Data entered successfully!!")

    def delete_data(self):
        """
        deletes data entry from the table if it exists

        :return: None
        """

        # `DELETE` operation
        delData = input("Enter name to delete its entry > ")
        query2 = "DELETE FROM students WHERE name = '{}'".format(delData)
        self.cursor.execute(query2)
        self.con.commit()

    def update_data(self, originalName: str, newName: str):
        """
        updates existing data in the table

        :param originalName: original data present in the table
        :param newName: changed data
        :return: None
        """

        # `UPDATE` operation
        query2 = "UPDATE students SET name='{}' WHERE name ='{}'".format(newName, originalName)
        self.cursor.execute(query2)
        self.con.commit()

    def display_data(self):
        query3 = "SELECT * FROM students"
        self.cursor.execute(query3)
        print(self.cursor.fetchall())


my_db = SQL()
wish = "y"
while wish.lower() != "n":

    print("Choose the correct option:")
    print("Press 1 to insert data in the table")
    print("Press 2 to delete data from table")
    print("Press 3 to update data in the table")
    print("Press 4 to display data entries")
    print("Press 0 to exit!")
    option = int(input("Enter option > "))

    if option == 1:
        my_db.insert_data()

    elif option == 2:
        my_db.delete_data()

    elif option == 3:
        oldData = input("Enter name to change > ")
        newData = input("Enter changed name > ")
        my_db.update_data(oldData, newData)

    elif option == 4:
        my_db.display_data()

    elif option == 0:
        break

    else:
        print("Invalid option!!")

    wish = input("Do you wish to continue? Enter y to continue, n to exit > ")

    if wish.lower() != 'y' and wish.lower() != 'n':
        print("Invalid option")
        wish = input("Enter y to continue, n to exit > ")
