import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS STUD(ROLL INTEGER PRIMARY KEY, NAME TEXT)""")
class Stud :
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
    def insert_stud(self):
        with conn:
            c.execute("INSERT INTO STUD VALUES(:ROLL,:NAME)",{'ROLL':self.roll, 'NAME':self.name})
    def get_stud(self):
        c.execute("SELECT * FROM STUD")
        return c.fetchall()
    def remove_stud(self):
        with conn:
            c.execute("DELETE FROM STUD WHERE ROLL=:ROLL AND NAME=:NAME",{'ROLL':self.roll,'NAME':self.name})

s1 = Stud(123,'ram')
s1.insert_stud()
print(s1.get_stud())
