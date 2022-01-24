import mysql.connector


def insert_path_to_db(path):
    mycursor.execute("INSERT IGNORE INTO images (path) VALUES (%s);", (path,))
    mydb.commit()


def update_label(path, label):
    print(path, label)
    mycursor.execute(
        "UPDATE images SET label = %s WHERE path = %s;", (label, path))
    mydb.commit()


mydb = mysql.connector.connect(
    host="localhost",
    user="imHD",
    password="",
    database="xray_images"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS xray_images;")
mydb.commit()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS images (path VARCHAR(255) PRIMARY KEY, label INTEGER);")
mydb.commit()
