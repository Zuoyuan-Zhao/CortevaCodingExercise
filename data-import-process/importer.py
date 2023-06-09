import os
import sys
import mysql.connector
import configparser
import logging


# Extract data from file and insert it into MySQL DB
def import_weather_file(file_path, location):
    # Setup DB configs
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
    failed_row_count = 0
    processed_row_count = 0;
    # read file and insert data into the table
    with open(file_path, "r") as f:
        for line in f:
            # extract data from line
            data = line.split()
            date = data[0]

            max_temp = float(data[1]) / 10.0 if float(data[1]) > -9999 else None
            min_temp = float(data[2]) / 10.0 if float(data[2]) > -9999 else None
            precipitation = float(data[3]) / 10.0 if float(data[3]) > -9999 else None
            try:
                # insert data into MySQL table
                query = '''
                        INSERT INTO Weather
                           (Location, DateStamp, MaxTemp, MinTemp, Precipitation)
                         VALUES
                           (%s, %s, %s, %s, %s)
                         ON DUPLICATE KEY UPDATE
                           MaxTemp       = VALUES(MaxTemp),
                           MinTemp       = VALUES(MinTemp),
                           Precipitation = VALUES(Precipitation)	
                        '''
                values = (location, date, max_temp, min_temp, precipitation)
                cursor.execute(query, values)
                processed_row_count = processed_row_count + 1
            except mysql.connector.IntegrityError as e:
                logging.debug("Encountered issue when inserting row: " + e.msg)
                failed_row_count = failed_row_count + 1
                pass

    # commit changes and close database connection
    db.commit()
    db.close()
    logging.info('Processed rows: ' + str(processed_row_count))
    if failed_row_count == 0:
        logging.info('Processed file: ' + file_path + ' with no failure')
    else:
        logging.info('Processed file: ' + file_path + ' with ' + str(failed_row_count) + ' failed rows')
    return processed_row_count


def process_files():
    config.read('config.ini')
    file_directory = config.get('ProcessorInfo', 'file_directory')
    failed_file_count = 0
    total_processed_count = 0;
    # Loop through all files in the folder and process it one by one
    for filename in os.listdir(file_directory):
        file_path = os.path.join(file_directory, filename)
        location = os.path.splitext(filename)[0]
        if os.path.isfile(file_path):
            try:
                logging.info('Processing file: ' + file_path)
                count = import_weather_file(file_path, location)
                total_processed_count = total_processed_count + count
            except:
                e = sys.exc_info()[0]
                logging.error('Failed to process file: ' + e)
                failed_file_count = failed_file_count + 1
                pass
    logging.info('Processed files with ' + str(failed_file_count) + ' failures')
    logging.info('Total rows processed: ' + str(total_processed_count))


# Setup logging
config = configparser.ConfigParser()
config.read('config.ini')
log_path = config.get('ProcessorInfo', 'log_path')
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Setup basic stats
logging.info('Process Starts')
process_files()
logging.info('Process Ends')
