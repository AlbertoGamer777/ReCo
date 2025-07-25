import os
import platform

def clear():
    if platform.platform=="Windows":
        os.system("cls")
    else:
        os.system("clear")

cnumber=int(input("Number of Tables: "))
aux0 = 0
columns = dict({})
ctrinner_template = ()
for i in range(1,cnumber+1)[::-1]:
    aux0 += 1
    ntname = str(input("New Table Name ("+format(aux0)+"/"+format(cnumber)+")"))
    ntdtype = str(input("Data Type of New Table ("+format(aux0)+"/"+format(cnumber)+")"))
    clear()
    columns[ntname] = ntdtype
    aux_keydict = list(columns)
    aux_cnumber = len(aux_keydict)
    if aux_cnumber != cnumber:
        print("Warning: The number of columns indicated to the program is not the same as the number of columns the number of columns supplied")
    
    print("Sub-step 1/2 Completed")


print("Form completed, sending instruction/s...")
aux1 = 0
for i in range(1,cnumber+1)[::-1]:
    print("""
                CREATE TABLE """,ntname,""" (
                """+ctrinner_template+""")
                """)