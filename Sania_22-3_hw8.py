# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий
# авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200
# символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2
# цифры поле плавающей точки, поле не должно быть пустым (NOT NULL) значением
# по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных размером 5 цифр, поле не должно
# быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
# 8. Добавить функцию, которая меняет количество товара по id
# 9. Добавить функцию, которая меняет цену товара по id
# 10. Добавить функцию, которая удаляет товар по id
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в
# консоли
# 12. Добавить функцию, которая бы выбирала из БД товары которые дешевле 100 сомов и
# количество которых больше чем 5 и распечатывала бы их в консоли

# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое
# слово “мыло”, должны соответствовать поиску товары с названием - “Жидкое мыло с
# запахом ванили”, “Мыло детское” и тд.)

import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_goods(conn, goods):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, goods)
        conn.commit()
    except Error:
        print(Error)


def update_products_quantity(conn, goods):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, goods)
        conn.commit()
    except Error:
        print(Error)

def update_products_price(conn, goods):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, goods)
        conn.commit()
    except Error:
        print(Error)

def delete_goods(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def select_all_goods(conn):
    try:
        sql = '''SELECT * FROM products '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
    except Error:
        print(Error)

def select_price_and_quantity_goods(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
    except Error:
        print(Error)

def select_goods_by_product_title(conn):
    try:
        sql = '''SELECT * FROM products WHERE (product_title LIKE  '%мыло%') OR (product_title LIKE  '%Мыло%')'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
    except Error:
        print(Error)

connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print("Connected Success!")
    # create_table(connection, create_products_table)
    # create_goods(connection, ('Жидкое мыло', 30.30, 30))
    # create_goods(connection, ('Детское мыло', 35.30, 40))
    # create_goods(connection, ('Мыло с запахом ванили', 30.40, 80))
    # create_goods(connection, ('Средство для мытья посуды', 60.30, 50))
    # create_goods(connection, ('Стиральный порошок', 900, 15))
    # create_goods(connection, ('Туалетная бумага', 90.60, 20))
    # create_goods(connection, ('Хозяйственное мыло', 50.30, 3))
    # create_goods(connection, ('Зубные щётки', 50.30, 12))
    # create_goods(connection, ('Крем для лица', 1000, 4))
    # create_goods(connection, ('Мицеллярная вода', 241.31, 1))
    # create_goods(connection, ('Шампунь', 250.42, 5))
    # create_goods(connection, ('Кондиционер для волос', 280.30, 3))
    # create_goods(connection, ('Мыло с запахом лаванды', 31.30, 6))
    # create_goods(connection, ('Шуманит', 50.30, 8))
    # create_goods(connection, ('Таблетки (карсулы) для посудомоечной машины', 160.26, 9))
    # update_products_quantity(connection, (12, 14))
    # update_products_price(connection, (196.64, 11))
    # create_goods(connection, ('Жидкое мыло', 30.30, 30))
    # delete_goods(connection, 16)
    # select_all_goods(connection)
    # select_price_and_quantity_goods(connection)
    # select_goods_by_product_title(connection)
    # create_goods(connection, ('Хозяйственное мыло запахом хвои', 50.30, 3))
    # select_goods_by_product_title(connection)

    print('Done!')