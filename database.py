import sqlite3
import os.path
from os import path

class Database:
    def __init__(self, filename="data.db"):
        self.new_db = False
        self.db_file = filename
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        if self.new_db:
            try:
                self.cur.execute("DROP TABLE IF EXISTS shortener")
                self.cur.execute("CREATE TABLE IF NOT EXISTS shortener (id INTEGER PRIMARY KEY, url TEXT NOT NULL)")
                self.conn.commit()
                self.new_db = False
            except sqlite3.Error as err:
                print(err)

    def insert(self, key, url):
        try:
            self.cur.execute("INSERT INTO shortener(id, url) VALUES(?, ?)", (key, url))
            self.conn.commit()
        except sqlite3.Error as err:
            print(err)
    
    def get(self, key):
        try:
            self.cur.execute("SELECT * FROM shortener where id=?", (key,))
            data = self.cur.fetchall()
            return data
        except sqlite3.Error as err:
            print(err)
    
    def delete(self, key):
        try:
            self.cur.execute("DELETE FROM shortener where id=?", (key,))
            self.conn.commit()
        except sqlite3.Error as err:
            print(err)
            
    def close(self):
        self.conn.close()

    def create_connection(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w"):
                pass
            self.new_db = True
        try:
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            print("DATABASE CONNECTED")
            return conn
        except sqlite3.Error as err:
            print(err)