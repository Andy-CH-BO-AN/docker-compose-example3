import mysql.connector


def test_db_connect():
    connection = mysql.connector.connect(
        user='readonly',
        password='password',
        host='stylish host',
        port="3306",
        database='stylish_backend'
    )

    cursor = connection.cursor()
    cursor.execute('Select name FROM stylish_backend.user ')
    results = cursor.fetchall()
    connection.close()

    assert results[0] == 'Ying Ngai'


test_db_connect()
