import sqlite3

database_file = "password.db"

def create_table_if_not_exists(table_name):
    try:
        conn = sqlite3.connect(database_file)  # Connect to the database.
        cursor = conn.cursor()  # Create a cursor object.

        # SQL statement to create a table IF NOT EXISTS
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_name TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
        cursor.execute(create_table_sql)  # Execute the SQL statement.

        conn.commit()  # Commit the changes.
        print(f"Table '{table_name}' created or already exists.")

    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

    finally:
        if conn:
            conn.close()  # Close the connection


def add_password(site_name, password): # Check to make sure that the site name doesnt already exists
    try:
      conn = sqlite3.connect(database_file)  # Connect to the database.
      cursor = conn.cursor()  # Create a cursor object.
      add_value_to_password_table = f""" INSERT INTO password (site_name, password) VALUES (?,?)"""
      cursor.execute(add_value_to_password_table,(site_name,password))
      conn.commit()
      print(f"'{site_name}' has been added to table.")
  
    except sqlite3.Error as e:
        print(f"error adding value to table: {e}")

    finally:
        if conn:
            conn.close()

def retrieve_password(site_name):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM password WHERE site_name = ?",(site_name,))
        selected_row = cursor.fetchall() 
        if len(selected_row) == 0:
            print(f"A password is not found for {site_name}")
        else: 
            print(f"password found {selected_row[0][2]}")
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"error querying table: {e}")
    
    finally:
        if conn:
            conn.close()

