import sqlite3

connection = sqlite3.connect('Avinash_Store.db')

cursor = connection.cursor()

# Creating table

store_command = """ CREATE TABLE IF NOT EXISTS 
stores(store_id INTEGER PRIMARY_KEY,location TEXT) """

cursor.execute(store_command)

# purchases table

purchases_command = """ CREATE TABLE IF NOT EXISTS  
purchases(purchase_id INTEGER PRIMARY_KEY,store_id INTEGER,cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id)) """

cursor.execute(purchases_command)

# Adding data to stores table

cursor.execute("INSERT INTO stores VALUES (1,'Binghamton,New York')")
cursor.execute("INSERT INTO stores VALUES (2,'San Francisco,California')")
cursor.execute("INSERT INTO stores VALUES (3,'Dublin,Ireland')")

# Retrieving data from the stores table

cursor.execute("SELECT * FROM stores WHERE location='San Francisco,California'")
print(cursor.fetchall())

# Adding data to the purchases table
cursor.execute("INSERT INTO purchases VALUES (101, 1, 50.0)")
cursor.execute("INSERT INTO purchases VALUES (102, 2, 75.99)")

# Retrieve specific information from the purchases
cursor.execute("SELECT * FROM purchases  WHERE purchase_id=101")
item1 = cursor.fetchone()
print(f"The item was purchased at {item1[1]} and cost ${item1[2]:.2f}")

cursor.execute("SELECT * FROM stores")
print(cursor.fetchall())


# Update an entry in the database
update_command = "UPDATE purchases SET cost = 54.99 where purchase_id = 101"
cursor.execute(update_command)


# Show that the update took place
cursor.execute("SELECT * FROM purchases WHERE  purchase_id = 101")
print(cursor.fetchone())

cursor.execute("SELECT * FROM purchases")
print(cursor.fetchall())


#Delete record from purchases
delete_command = "DELETE FROM purchases WHERE  purchase_id = 101"
cursor.execute(delete_command)
print(cursor.rowcount,"record deleted.")

#Confirm that the record is no longer in the database
cursor.execute("SELECT COUNT(*) FROM purchases WHERE purchase_id = 101")
print(cursor.fetchone())