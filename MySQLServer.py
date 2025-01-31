import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',      
            password='Brian@024.'  
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Creating the database (if it doesn't already exist)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Catching specific MySQL errors
        print(f"MySQL Error: {e}")
    
    except Exception as e:  # Catching other non-MySQL errors
        print(f"Error: {e}")
    
    finally:
        # Closing the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
