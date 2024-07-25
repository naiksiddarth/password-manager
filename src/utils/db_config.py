import mysql.connector # type: ignore
import rich.console
rconsole = rich.console.Console()

def dbconfig():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='password'
        )
    except Exception as e:
        rconsole.print_exception()
    return db