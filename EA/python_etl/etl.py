# python modules
import mysql.connector
import pyodbc
import fdb

# variables
from EA.python_etl.variables import datawarehouse_name


def etl(query, source_cnx, target_cnx):
    # extract data from source db
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # load data into warehouse db
    if data:
        target_cursor = target_cnx.cursor()
        target_cursor.execute("USE {}".format(datawarehouse_name))
        target_cursor.executemany(query.load_query, data)
        print('data loaded to warehouse db')
        target_cursor.close()
    else:
        print('data is empty')

def etl(query, source_cnx, target_cnx):
    # extract data
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)

    data = source_cursor.fetchall()
    source_cursor.close()

    if data:
        cursor= target_cnx.cursor()
        cursor.execute("USE {}".format(datawarehouse_name))
        cursor.executemany(query.load_query, data)

        print('data loaded to warehouse db')
        cursor.close
    else:
        print('data is empty')



def etl_process(queries, target_cnx, source_db_config, db_platform):
    # establish source db connection
    if db_platform == 'mysql':
        source_cnx = mysql.connector.connect(**source_db_config)
    elif db_platform == 'sqlserver':
        source_cnx = pyodbc.connect(**source_db_config)
    elif db_platform == 'firebird':
        source_cnx = fdb.connect(**source_db_config)
    else:
        return 'Error! unrecognised db platform'

    # loop through sql queries
    for query in queries:
        etl(query, source_cnx, target_cnx)

    # close the source db connection
    source_cnx.close()

def etl_process(queries, target_cnx, source_db_config, db_platform):
    if db_platform == 'mysql':
        source_cnx = mysql.connector.connect(**source_db_config)
    elif db_platform == 'sqlserver':
        source_cnx = pyodbc.connect(**source_db_config)
    else:
        return 'Error! unrecognized db'

    for query in queries:
        etl(query, source_cnx, target_cnx)
        cursor = source_cnx.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        if data:
            cursor= target_cnx.cursor()
            cursor.execut("USE {}".format(databasename))
            cursor.execut(quere.load_query, data)
            cursor.close()

    source_cnx.close()
