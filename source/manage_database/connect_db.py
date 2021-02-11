import json
import mysql.connector

from settings import MYSQL_CREDENTIAL_PATH


def connect_db():

    json_file = open(MYSQL_CREDENTIAL_PATH)
    credential = json.load(json_file)
    db_host = credential["host"]
    db_database = credential["dbname"]
    username = credential['username']
    password = credential['password']

    mark_db = mysql.connector.connect(

        host=db_host,
        user=username,
        password=password,
        database=db_database
    )

    return mark_db
