import os
import sys
import mysql.connector
import configparser
import logging


def pull_avg(query):
    # Setup DB configs
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

    # Execute the query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()[0]

    # Close the cursor and the database connection
    cursor.close()
    db.close()

    return result


def pull_avg_min(location, year):
    min_query_template = 'SELECT AVG(MinTemp) FROM Weather WHERE Location = \'{}\' AND YEAR(DateStamp) = {};'
    min_query = min_query_template.format(location, year)
    return pull_avg(min_query)


def pull_avg_max(location, year):
    max_query_template = 'SELECT AVG(MaxTemp) FROM Weather WHERE Location = \'{}\' AND YEAR(DateStamp) = {};'
    max_query = max_query_template.format(location, year)
    return pull_avg(max_query)


print(pull_avg_min('USC00110072', '1985'))
print(pull_avg_max('USC00110072', '1985'))

