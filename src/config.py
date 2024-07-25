from utils.db_config import dbconfig
# import rich
from rich import print as printc
import random
import hashlib
import sys
import getpass
import string

def debug():
    print("here")
debug()
# console = rich.console.Console()

def generate_device_secret(length):
    ds = random.choices(string.ascii_uppercase + string.digits, k = length)
    return ds

def config():
    db = dbconfig()
    cursor = db.cursor()
    printc("[green][+] Creating a database [/green]")
    try:
        cursor.execute("CREATE DATABAsE pm")
    except Exception as e:
        printc("[red][!] could not create a databse")
        # console.print_exception(e)
        print(e)
        sys.exit(0)
    printc("[green][+] Database created [/green]")
    #creating tables
    query = "CREATE TABLE pm.secrets(masterkey_hash TEXT NOT NULL, device_secrets TEXT NOT NULL)"
    cursor.execute(query)
    printc("[green][+]Table 'secrets' created[/green]")

    query = "CREATE TABLE pm.entries(site_name TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT NOT NULL, hash TEXT NOT NULL)"
    cursor.execute(query)
    printc("[green][+]Table 'entries' created[/green]")

    mp = ''
    while True:
        mp = getpass.getpass("Enter a Master Password : ")
        if mp == getpass.getpass("Retype your Master Password : ") and mp != '':
            break
        printc("[red][!]Try again[/red]")

    mp = hashlib.sha256(mp.encode()).hexdigest()
    ds = generate_device_secret(10)
    str_ds = ''
    
    for ele in ds:
        str_ds += ele

    cursor.execute("INSERT INTO pm.secrets (masterkey_hash,device_secrets) VALUES(%s,%s)",(mp,str_ds))
    db.commit()
    printc("[green][+] Added Master password and device secret to database[/green]")
    printc("[green][+]Password Manager configuratio done [/green]")

    db.close()

config()