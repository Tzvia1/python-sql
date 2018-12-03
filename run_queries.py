import sqlite3
import csv
import json
from Query import Query

PATH = 'C:\sqlite/'

class Connection:
    def __init__(self,db_str):
        self.db = sqlite3.connect(db_str)
        #self.cursor = self.db.cursor()

    def __del__(self):
        #self.cursor.close()
        self.db.close()

def query_to_csv(query,db):
   cursor = db.cursor()
   cursor.execute(query.query_txt)
   rows = cursor.fetchall()
   headers = [col[0] for col in cursor.description]
   fp = open(PATH+query.query_name+'.csv', 'w',encoding="utf-8")
   myFile = csv.writer(fp, lineterminator='\n')
   myFile.writerow(headers)
   myFile.writerows(rows)
   fp.close()


def query_to_tbl(query,db):
    cursor = db.cursor()
    cursor.execute('drop table if exists '+query.query_name)
    cursor.execute('create table '+query.query_name+' as '+query.query_txt)
    cursor.close()

def query_to_json(query, db):
    cursor = db.cursor()
    results = cursor.execute(query.query_txt)
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in results]
    file = open(PATH+query.query_name+'.json', 'w')
    print(json.dumps({'items': items}), file=file)
    file.close()
    cursor.close()

def query_to_xml(query, db):
    cursor = db.cursor()
    results = cursor.execute(query.query_txt)
    rows = [dict(zip([key[0] for key in cursor.description], row)) for row in results]
    file = open(PATH+query.query_name+'.xml', 'w', encoding="utf-8")
    print('<data>', file=file)
    for row in rows:
        print('<row>', file=file)
        for k, v in row.items():
            print('<' + k + '>' + str(v) + '</' + k + '>', file=file)
        print('</row>', file=file)
    print('</data>', file=file)
    file.close()
    cursor.close()


def run_queries(str_con, output):
    con = Connection(str_con)


    for i in range(7):
        query = Query(i+1)
        if output =='csv':
            query_to_csv(query, con.db)
        elif output =='json':
            query_to_json(query, con.db)
        elif output == 'tbl':
            query_to_tbl(query, con.db)
        elif output == 'xml':
            query_to_xml(query, con.db)

    del con
    print('end of run queries to '+output)
