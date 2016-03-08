# config.py
# Configuation file for the database connection

database = 'database_name'
username = 'database_user'
password = 'database_pass'
client_secrets_path = '/path/to/secrets.json'


def connectionString():
    return "postgresql+psycopg2://" + username + ":" + password + "@/" + database


def clientSecrets():
    return client_secrets_path
