import mysql.connector # type: ignore
import rich

console = rich.Console

def dbconfig():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='password'
        )
    except Exception as e:
        console.print_exception(e)
                
    return db