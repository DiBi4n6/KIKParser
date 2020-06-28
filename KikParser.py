#KIKParser to parse Email Address, DisplayName, and Username from KIK database
import csv
import sqlite3
import time


print()
print ("This script will parse the Email Adress")
print ("DisplayName and UserName from a KIK database!")
print()

time.sleep(5)

db = sqlite3.connect("4886a0b8-37a0-4466-b952-b83061c70685.kikDatabase.db")

csv_file = open('KIKParser.csv','w')
writer = csv.writer(csv_file)


data_headers = ('EmailAddress', 'DisplayName', 'Username')

writer.writerow(data_headers)

for row in db.execute('SELECT jid, display_name, user_name FROM KIKcontactsTable'):
    print(row)
    writer.writerow(row)


db.close()






	

	
