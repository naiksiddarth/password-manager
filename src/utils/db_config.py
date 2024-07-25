import mysql.connector # type: ignore
import rich



def dbconfig():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='password'
        )
    except Exception as e:
        print(e)

    return db