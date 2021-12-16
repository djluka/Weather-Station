import mysql.connector
from mysql.connector import Error

def mysql_conn():
    try:
        return mysql.connector.connect(
                host='localhost',
                port=8081,
                user='temp',
                passwd='temp',
                database='temp')
    except Error as err:
        print(f"Error: '{err}'")
        raise err

def create_table(conn):
    query = """
    CREATE TABLE temperature (
        id INT AUTO_INCREMENT,
        temperature FLOAT NOT NULL,
        humidity INT NOT NULL,
        pressure FLOAT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id)
    )"""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
    except Error as err:
        print(f"Error: '{err}'")

def insert_data(conn, temperature, humidity, pressure):
    query = "INSERT INTO `temperature` (`temperature`, `humidity`, `pressure`) VALUES(%s, %s, %s)"
    values = (temperature, humidity, pressure)

    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
    except Error as err:
        print(f"Error: '{err}'")

def get_recent_temperature(conn):
    query = "SELECT `temperature`, `humidity`, `pressure`, `timestamp` FROM `temperature` ORDER BY `timestamp` DESC LIMIT 1"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        response = {}
        response['temperature'] = record[0]
        response['humidity'] = record[1]
        response['pressure'] = record[2]
        response['date'] = record[3]

        cursor.close()
    
        return response
    except Error as err:
        print(f"Error: `{err}`")
