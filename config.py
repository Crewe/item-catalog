# dbconfig.py
# Configuation file for the database connection

database = 'database_name'
username = 'database_user'
password = 'database_pass'
app_path = '/path/to/app'
client_secrets_path = '/path/to/secrets.json'


def connectionString():
    return "postgresql+psycopg2://" + username + ":" + password + "@/" + database


def appPath():
    return app_path


def clientSecrets():
    return secrets_path
