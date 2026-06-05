import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # XAMPP default password is empty
    database="studentdb"
)

cursor = db.cursor()

# User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

# Confirmation
print("\nPlease confirm your details:")
print("Name:", name)
print("Age:", age)
print("Email:", email)
print("Address:", address)

confirm = input("\nAre you sure? (yes/no): ")

if confirm.lower() == "yes":

    sql = """
    INSERT INTO users (name, age, email, address)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, email, address)

    cursor.execute(sql, values)

    db.commit()

    print("\nData inserted successfully!")

else:
    print("\nCancelled.")

# Close connection
cursor.close()
db.close()