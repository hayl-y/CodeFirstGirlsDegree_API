import configparser

config = configparser.ConfigParser()

config.read('config_db.ini')

# value = config.get('section_name', 'option_name')
database_host = config.get('Database', 'host')
database_port = config.get('Database', 'port')
database_name = config.get('Database','database')
database_username = config.get('Database', 'username')
database_password = config.get('Database', 'password')

print(f"Database Host: {database_host}")
print(f"Database Port: {database_port}")
print(f"Database Name: {database_name}")
print(f"Database Username: {database_username}")
print(f"Database Password: {database_password}")

config.set('Database', 'password', 'new_password')

with open('config.ini', 'w') as configfile:
 config.write(configfile)