import mysql.connector
import os

def backup_mysql_db(host, user, password, database, backup_file):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Create a cursor object just add comment here
#COMMENT BY AMMU
    cursor = connection.cursor()

    # Dump the database using mysqldump command (You need to have mysqldump installed)
    backup_cmd = f"mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}"
    os.system(backup_cmd)

    # Close the connection
    cursor.close()
    connection.close()

# Usage
backup_mysql_db("localhost", "root", "password", "my_database", "backup.sql")

