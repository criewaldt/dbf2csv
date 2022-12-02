from simpledbf import Dbf5
import os, csv

from dbfread import DBF
DBF_LOCATION = os.path.abspath("COMPANY.dbf")
CSV_LOCATION = "COMPANY.csv"

with open(CSV_LOCATION, 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for row in DBF(DBF_LOCATION):
        if count == 0:
            writer.writerow(dict(row))
            writer.writerow(dict(row).values())
            count += 1
        else:
            writer.writerow(dict(row).values())
#DBF_LOCATION = os.path.abspath("COMPANY.dbf")
#dbf = Dbf5(DBF_LOCATION, codec='utf-8')
#dbf.to_csv('COMPANY.csv')
