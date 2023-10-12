import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=8889
)

# print(mydb)

# CREATING A DATABASE
mycursor = mydb.cursor()


# SHOW DATABASES
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)


# INSERT INTO
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
