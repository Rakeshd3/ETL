import pyodbc
cnxn = pyodbc.connect(r"Driver={SQL Server};"
                      r"Server=rakesh1988;"
                      r"Database=myaccount;"
                      r"Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM myexpenditure')