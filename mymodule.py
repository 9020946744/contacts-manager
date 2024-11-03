import sqlite3

class Database:
    
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute( """
                            CREATE TABLE IF NOT EXISTS Contacts ( name text, family text, score float)
                            """)
        self.con.commit()
        
        
    def insert(self, name, family, score):
   
        self.cur.execute("""
                            INSERT INTO Contacts VALUES( ?, ?, ?)
                            """, (name, family, score))
        self.con.commit()


