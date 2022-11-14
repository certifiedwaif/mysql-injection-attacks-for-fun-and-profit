from mysql.connector import connect


def main():
    with connect(
        host="mysql-server",
        user='user',
        password='password'
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('USE db')
            cursor.execute('DROP TABLE users')
            create_table_sql = """
            CREATE TABLE users(
                user varchar(100) not null,
                password varchar(100) not null
            )
            """
            cursor.execute(create_table_sql)
            cursor.execute("INSERT INTO users VALUES('mark', 'secret')")
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchmany()
            print(users)
            user = input('Which user would you like the details for?')
            query = f"SELECT * FROM users WHERE user = '{user}'"
            print(query)
            cursor.execute(query)
            result = cursor.fetchmany()
            print(result)


if __name__ == "__main__":
    main()