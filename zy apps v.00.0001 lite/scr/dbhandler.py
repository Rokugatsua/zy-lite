import config
import sqlite3, os 
from sqlite3 import Error

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] =  super(Singleton, cls).__call__(*args, **kwargs)
        #else:
            #cls._instances[cls].__init__(*args, *kwargs)
        return cls._instances[cls]

class io:
    class create_the:
        def _enofa_ref(self):
            table_name = "enofa_ref"
            stmnt = """CREATE TABLE IF NOT EXISTS {} (
                id integer PRIMARY KEY,
                tname text NOT NULL UNIQUE,
                ref text NOT NULL,
                awal text NOT NULL,
                akhir text NOT NULL
                );""".format(str(table_name))
            d = db()
            d.create_table(stmnt)

        def _enofa_list(self, tname):
            table_name = tname
            print(table_name)
            stmnt = """CREATE TABLE IF NOT EXISTS {} (
                enofa integer PRIMARY KEY,
                has_record integer NOT NULL
                );""".format(str(table_name))
            d = db()
            d.create_table(stmnt)

    class insert_to:
        def _enofa_ref(self, data):
            table_name = "enofa_ref"
            stmnt =  """ INSERT INTO {} (
                tname,ref,awal,akhir)
                VALUES(?,?,?,?)""".format(str(table_name))
            d = db()
            d.insert_into(stmnt, data)

        def _enofa_lists(self, tname, data):
            print("insert")
            table_name = tname
            stmnt = """ INSERT INTO {}
                    (enofa,has_record)
                    VALUES(?,?)""".format(str(table_name))
            
            #to exucemany()
            has_record = 0 # defaulf 0 is False
            datali = []
            for li in data:
                val = (li, has_record)
                datali.append(val)

            d = db()
            d.inserts_into(stmnt, datali)


    class select_from:
        def _enofa_ref(self):
            table_name = "enofa_ref"
            stmnt =""" SELECT * FROM {}""".format(str(table_name))
            
            d = db()
            data = d.select_from(stmnt)

            datali = []
            for li in data:
                datali.append(li)

            return datali
        
        def _enofa_lists(self,tname):
            table_name = tname
            stmnt =""" SELECT * FROM {}""".format(str(table_name))
            data = []
            print(stmnt)
            try:
                d = db()
                data = d.select_from(stmnt)
            except Error as e:
                print(e)

            datali = []
            for li in data:
                datali.append(li)

            return datali

    class update_of:
        def _enofa_lists(self, tname, data):
            table_name = tname
            stmnt = """UPDATE {} SET has_record = ? WHERE enofa= ?""".format(str(table_name))
            
            #to exucemany()
            has_record = 1 # defaulf 1 is True
            datali = []
            for li in data:
                print li
                val = (has_record,li)
                datali.append(val)
            try:
                d = db()
                d.updates_of(stmnt, datali)
            except Error as e:
                print(e)




class db:
    __metaclass__ = Singleton

    def __init__(self):
        try:
            databasefile =  os.path.join(config.cfgDir.dbdir, "database.db")
            self.conn = sqlite3.connect(databasefile)
        except Error as e:
            print(e)

    def create_table(self, stmnt):
        cur = self.conn.cursor()
        cur.execute(stmnt)
        self.conn.commit()

    def insert_into(self, stmnt, data):
        cur =  self.conn.cursor()
        cur.execute(stmnt, data)
        self.conn.commit()
    
    def inserts_into(self, stmnt, data):
        cur =  self.conn.cursor()
        cur.executemany(stmnt, data)
        self.conn.commit()

    def select_from(self, stmnt):
        cur = self.conn.cursor()
        cur.execute(stmnt)

        f = cur.fetchall()

        return f
    
    def updates_of(self, stmnt, data):
        cur = self.conn.cursor()
        cur.executemany(stmnt, data)
        self.conn.commit()
