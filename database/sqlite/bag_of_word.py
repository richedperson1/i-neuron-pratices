import os
import logging as lg
import re
import csv
import sqlite3

class home_word:
    patten = '[a-zA-Z]'
    lg.basicConfig(filename="homework.log", level=lg.INFO,
                   format="%(levelname)s %(asctime)s %(message)s")

    def __init__(self, filename:list[str]):
        """
        Filename must consist on all file name

        """
        self.file_name = filename

    def counting_word(self):
        """
        Counting the each word present in all five document and then increase it's count in dictionary

        """
        try:
            dist = {}
            for file in self.file_name:
                try:
                    """
                    We are opening with data file folder here ...!
                    """
                    with open(f"./data_file/{file}") as f:
                        data = f.read()
                        for word in data.split():
                            if word in dist:
                                dist[word] += 1
                            else:
                                dist[word] = 1
                except Exception as e:
                    lg.error(str(e))
                    lg.error(f"The filename is : {file}")
            return list(dist.items())
        except Exception as e:
            lg.exception(str(e))
            return e

    def counting_char(self):
        """
        Counting first character's of the word 
        """
        try:
            word_count = self.counting_word()

            character_count = {}
            for key, value in word_count:
                char = key[0]
                if bool(re.match(self.patten, char)):
                    if char in character_count:
                        character_count[char] += (value)
                    else:
                        character_count[char] = 1
            return list(character_count.items())
        except Exception as e:
            lg.error(str(e))
            return e

    def data_filter(self,filename,mini_char = 3):
        """
        filename: Name of unfilter file name in our case : vocab.pubmed.txt

        Filtering out Punctuation and other character number and only 
        give word 

        """
        try:
            patten =  "[a-zA-Z]{"+str(mini_char)+",}"
            # lg.info(patten)
            with open(f"./data_file/{filename}",'r',encoding="utf-8") as f:
                match = re.findall(patten,f.read())
            return match
        except Exception as e:
            lg.error(str(e))
            return e 

    def zipping_word_in_sqlite(self,database,table_name):
        # q4 = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB . 
        # (aah,>=,354,fdsf,wer)
        try:

            lst = os.listdir("./data_file")
            f1 = csv.reader( open("./data_file/"+lst[0],'r',encoding='utf-8'))
            f2 = csv.reader(open("./data_file/"+lst[1],'r',encoding='utf-8'))
            f3 = csv.reader(open("./data_file/"+lst[2],'r',encoding='utf-8'))
            f4 = csv.reader(open("./data_file/"+lst[3],'r',encoding='utf-8'))
            f5 = csv.reader(open("./data_file/"+lst[4],'r',encoding='utf-8'))
            j = 0
            db = sqlite3.connect(database)
            cur = db.cursor()
            for a1,a2,a3,a4,a5 in zip(f1,f2,f3,f4,f5):
                query = f'INSERT INTO {table_name} values("{a1[0]}","{a2[0]}","{a3[0]}","{a4[0]}","{a5[0]}")'
                # print(query)
                # break
                cur.execute(query)
                j+=1
            db.commit()
            lg.info("Data successfully added :)")
            print('Data successfully added 😍😍😍')
        except Exception as e:
            lg.exception(str(e))
            lg.error(str(e))
            return e



lst = os.listdir('./data_file/')
rutvik = home_word(lst)
rutvik.zipping_word_in_sqlite("five_file.db",'zipping')
# print(lst)
