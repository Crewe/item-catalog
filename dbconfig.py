# dbconfig.py
# Configuation file for the database connection

database = 'database_name'
username = 'database_user'
password = 'database_pass'


def connectionString():
    return "postgresql+psycopg2://" + username + ":" + password + "@/" + database
