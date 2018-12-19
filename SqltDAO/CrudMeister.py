import sqlite3


class Employee:

    def __init__(self):
        self.db = './CrudMeister.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('Name', 'Text'), ('Email1', 'Text'), ('Email2', 'Text'), ('Email3', 'Text'), ('Phone1', 'Text'), ('Phone2', 'Text'), ('Phone3', 'Text'), ('Notes', 'Text')]
        self.table_name = 'Employee'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM Employee;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS Employee;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS Employee(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name Text, Email1 Text, Email2 Text, Email3 Text, Phone1 Text, Phone2 Text, Phone3 Text, Notes Text);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO Employee ( Name, Email1, Email2, Email3, Phone1, Phone2, Phone3, Notes) VALUES (?,?,?,?,?,?,?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from Employee WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='Employee.csv', hasHeader=True, sep='","'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    if dao.insert(line.split(sep)) is False:
                        return False
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    

import sqlite3


class Principal:

    def __init__(self):
        self.db = './CrudMeister.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('Name', 'Text'), ('Email1', 'Text'), ('Email2', 'Text'), ('Email3', 'Text'), ('Phone1', 'Text'), ('Phone2', 'Text'), ('Phone3', 'Text'), ('Notes', 'Text')]
        self.table_name = 'Principal'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM Principal;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS Principal;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS Principal(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name Text, Email1 Text, Email2 Text, Email3 Text, Phone1 Text, Phone2 Text, Phone3 Text, Notes Text);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO Principal ( Name, Email1, Email2, Email3, Phone1, Phone2, Phone3, Notes) VALUES (?,?,?,?,?,?,?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from Principal WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='Principal.csv', hasHeader=True, sep='","'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    if dao.insert(line.split(sep)) is False:
                        return False
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    

import sqlite3


class Event:

    def __init__(self):
        self.db = './CrudMeister.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('Name', 'Text'), ('Start', 'Text'), ('Stop', 'Text')]
        self.table_name = 'Event'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM Event;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS Event;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS Event(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name Text, Start Text, Stop Text);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO Event ( Name, Start, Stop) VALUES (?,?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from Event WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='Event.csv', hasHeader=True, sep='","'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    if dao.insert(line.split(sep)) is False:
                        return False
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    

import sqlite3


class ToDo:

    def __init__(self):
        self.db = './CrudMeister.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('Name', 'Text'), ('Description', 'Text')]
        self.table_name = 'ToDo'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM ToDo;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS ToDo;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS ToDo(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name Text, Description Text);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO ToDo ( Name, Description) VALUES (?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from ToDo WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='ToDo.csv', hasHeader=True, sep='","'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    if dao.insert(line.split(sep)) is False:
                        return False
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    

import sqlite3


class Entry:

    def __init__(self):
        self.db = './CrudMeister.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('DateTime', 'Text'), ('ObjectName', 'Text'), ('ObjectId', 'Integer'), ('Description', 'Text')]
        self.table_name = 'Entry'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM Entry;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS Entry;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS Entry(ID INTEGER PRIMARY KEY AUTOINCREMENT, DateTime Text, ObjectName Text, ObjectId Integer, Description Text);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO Entry ( DateTime, ObjectName, ObjectId, Description) VALUES (?,?,?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from Entry WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='Entry.csv', hasHeader=True, sep='","'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    if dao.insert(line.split(sep)) is False:
                        return False
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    

