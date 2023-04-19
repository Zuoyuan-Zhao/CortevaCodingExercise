import mysql.connector
import configparser

from mysqlx import Error


def calculate_stats():
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config.get('Database', 'host')
    port = config.getint('Database', 'port')
    user = config.get('Database', 'user')
    password = config.get('Database', 'password')
    database = config.get('Database', 'database')

    # Connect to DB
    db = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = db.cursor()
    cursor.callproc('calculate_weather_stats')
    db.commit()

    cursor.close()
    db.close()


calculate_stats()

