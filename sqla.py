import psycopg
import platform
import os

def clear():
    if platform.platform=="Linux":
        os.system("cls")
    else:
        os.system("clear")

def menudet():
    print("""Database Editting Tools Menu
        0)Create Table
        """)
    if seldet==0:
        cnumber=int(input("Number of Tables: "))
        aux0 = 0
        columns = dict({})
        for i in range(1,cnumber+1)[::-1]:
            aux0 += 1
            ntname = str(input("New Table Name (",aux0,"/",cnumber,")"))
            ntdtype = str(input("Data Type of New Table (",aux0,"/",cnumber,")"))
            clear()
            columns[ntname] = ntdtype
            print("Form completed, sending instruction/s...")

        aux1 = 0
        for i in range(1,cnumber+1)[::-1]:
            with psycopg.connect("dbname=",database," user=",svuser) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                            CREATE TABLE """,ntname,""" (
                            )
                            """)
        for i in range(1,cnumber+1)[::-1]:
            with psycopg.connect("dbname=",database," user=",svuser) as conn:
                    cur.execute(
                        "INSERT INTO test (num, data) VALUES (%s, %s)",
                        (100, "abc'def"))

    elif seldet==2:
        with psycopg.connect("dbname=",database," user=",svuser) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO test (num, data) VALUES (%s, %s)",
                    (100, "abc'def"))

print("Welcome to SQLite portable CLI managing platform")

while True:
    clear()
    print("""Options:
          0)Server & Database Connection.
          1)Database Visualizing Tools.
          2)Database Editting Tools.
          3)Exit.""")

    sel=str(input("Option: "))
    clear()
    if sel==0:
        server=str(input("Server: "))
        database=str(input("Database name: "))
        svuser=str(input("User: "))
    elif sel==1:
        seldvt=str(input("Option for DVT: "))
         menudvt()
    elif sel==2:
        seldet=str(input("Option for DET: "))
        menudet()
    elif sel==3:    
        break
    else:
        clear()
        print("Invalid selection")
        ok=input("... Press any key")

