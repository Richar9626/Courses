import mysql.connector

# Step 3: Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host='your_host',           # e.g., 'localhost'
        user='your_username',       # e.g., 'root'
        password='your_password',   # e.g., 'password'
        database='your_database'    # e.g., 'employees_db'
    )

    if connection.is_connected():
        print("Successfully connected to the database")

    # Step 4: Create a cursor object
    cursor = connection.cursor()

    # Step 5: Write the SQL query
    query = "SELECT id, title, group FROM dashboard WHERE result = "FAIL";"

    # Step 6: Execute the query
    cursor.execute(query)

    # Step 7: Fetch the results and returns a list of tuples
    results = cursor.fetchall()

    # Step 8: Process the results
    for (id, title, group) in results:
        print(f"ID: {id}, Test: {title}, Test Group: {group}")

except mysql.connector.Error as error:
    print(f"Error connecting to MySQL: {error}")
finally:
    # Step 9: Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")