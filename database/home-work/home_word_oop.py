import pandas as pd
import mysql.connector as con
import logging as lg
import csv


class query:
    """
    Configuring log file with query class... 🤩
    """
    lg.basicConfig(filename='Dumping_data.log', level=lg.INFO,
                   format='%(levelname)s %(asctime)s %(message)s')

    def __init__(self, raw_data_file, sql_database) -> None:
        """
        Initilizing raw_data file and sql file name so that operation can be done on this 
        ☺ ☺ ☺
        """

        try:
            self.raw_data_file = raw_data_file
            self.sql_database = sql_database
        except Exception as e:
            lg.error(str(e))

    def bridge(self):
        """
        Making connection between Database and Python 🐍🐍🐍
        """
        try:
            self.mydb = con.connect(
                host='localhost', user='root', passwd='ru15070610', database=self.sql_database)
            self.cur = self.mydb.cursor()
        except Exception as e:
            lg.error(str(e))

    def command(self, query):

        try:
            self.bridge()
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as e:
            lg.error(str(e))

    def insert(self, table_name):
        """
        This class method used for inserting value into sql table from data file
        """
        with open(self.raw_data_file) as f:
            try:
                self.bridge()
                car_data = csv.reader(f, delimiter='\n')
                for sent in car_data:
                    sent = sent[0].split(',')
                    query = f'insert into {self.sql_database}.{table_name} values({[str(a) for a in sent ]})'
                    query = query.replace('[', '')
                    query = query.replace(']', '')
                    self.cur.execute(query)
                self.mydb.commit()

            except Exception as e:
                print(e)
                lg.error(str(e))
                lg.exception(str(e))

    def checking_data(self):
        table_name = self.command(f"describe car_details")
        print(len(table_name))

    # @command()
    # def create_database(query):
    #     return query

    def __str__(self) -> str:
        return  "Author : rutvikjaiswal195@gmail.com"

rutvik = query('car.data','car_data')
rutvik.checking_data()
