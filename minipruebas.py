import os
import platform

def clear():
    if platform.platform=="Windows":
        os.system("cls")
    else:
        os.system("clear")

ntname = str(input("New Table Name: "))
cnumber=int(input("Number of Columns: "))
aux0 = 0
ctrinner_template = ("")
for i in range(1,cnumber+1)[::-1]:
    aux0 += 1
    ncname = str(input("New Column Name ("+format(aux0)+"/"+format(cnumber)+"): "))
    ncdtype = str(input("Data Type of New Column ("+format(aux0)+"/"+format(cnumber)+"): "))
    ncaargument = str(input("New Column Aditional Argument ("+format(aux0)+"/"+format(cnumber)+") (Press enter if not): "))
    clear()
    ctrinner_template += (ncname + " " + ncdtype + " " + ncaargument + """
            """)
    print("Sub-step 1/2 Completed")
print("Form completed, sending instruction/s...")
aux1 = 0
print("""
            CREATE TABLE """,ntname,""" (
            """+ctrinner_template+""")
            """)