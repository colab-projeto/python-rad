import mysql.connector

# Example of creating a connection to a MySQL database
cnx = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Example of creating a cursor object to execute SQL queries
cursor = cnx.cursor()

# Example of executing a query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()
