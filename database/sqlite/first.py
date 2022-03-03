from functools import reduce
import os
import logging as lg
import re
import csv
import sqlite3

lst = os.listdir("./data_file")

# q4 = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB . 
# (aah,>=,354,fdsf,wer)


f1 = csv.reader( open("./data_file/"+lst[0],'r',encoding='utf-8'))
f2 = csv.reader(open("./data_file/"+lst[1],'r',encoding='utf-8'))
f3 = csv.reader(open("./data_file/"+lst[2],'r',encoding='utf-8'))
f4 = csv.reader(open("./data_file/"+lst[3],'r',encoding='utf-8'))
f5 = csv.reader(open("./data_file/"+lst[4],'r',encoding='utf-8'))

# db = sqlite3.connect("fetching.db")
# cur = db.cursor()
# query = "CREATE table zipping(f1 text,f2 text,f3 text,f4 BLOB,f5 text)"
# query = "select * from zipping"
# cur.execute(query)
# print(cur.fetchall())


for a1,a2,a3,a4,a5 in zip(f1,f2,f3,f4,f5):
    print(a1,a2,a3,a4,a5)
    print(f'"{a1[0]}","{a2[0]}","{a3[0]}","{a4[0]}","{a5[0]}")')

    break