from pymysql import connect, cursors


HOST_DB = "localhost"
PASSWORD_DB = "toro"
USER_DB = "root"
NAME_DB = "toro"
PORT_DB = 3306

connection = connect(
    host=HOST_DB,
    port=PORT_DB,
    user=USER_DB,
    password=PASSWORD_DB,
    database=NAME_DB,
    cursorclass=cursors.DictCursor
)

cursor = connection.cursor()

assets = open('docker/backend/datas/assets.sql', "r")
assets = assets.read()
cursor.execute(assets)

users = open('docker/backend/datas/users.sql', "r")
users = users.read()
cursor.execute(users)

accounts = open('docker/backend/datas/accounts.sql', "r")
accounts = accounts.read()
cursor.execute(accounts)

user_assets = open('docker/backend/datas/user_assets.sql', "r")
user_assets = user_assets.read()
cursor.execute(user_assets)

orders = open('docker/backend/datas/orders.sql', "r")
orders = orders.read()
cursor.execute(orders)

connection.commit()
