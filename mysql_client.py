from mysql.connector import connect


def main():
    with connect(
        host="mysql-server",
        user='user',
        password='password'
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE db')
            cursor.execute('USE db')
            create_table_sql = """
            CREATE TABLE users(
                user varchar(100) not null,
                password varchar(100) not null
            )
            """
            cursor.execute(create_table_sql)
            cursor.execute("INSERT INTO TABLE VALUES('mark', 'secret')")
            user = input('Which user would you like the details for?')
            cursor.execute(f'SELECT {user} FROM users')
            result = cursor.fetchmany()
            print(result)


if __name__ == "__main__":
    main()