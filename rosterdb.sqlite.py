import sqlite3
import json
import os
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "rosterdb.sqlite")
data_path = os.path.join(base_path, "roster_data.json")
conn = sqlite3.connect (db_path)
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Member (
    user_id  INTEGER,
    course_id INTEGER,
    role  Integer,
    PRIMARY KEY (user_id , course_id)
);

''')
if not os.path.exists(data_path):
    data_path = "roster_data_sample.json"

with open(data_path) as f:
    str_data = f.read()



json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print((name , title, role))
    

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute ('INSERT OR REPLACE INTO Member (user_id , course_id , role) VALUES (? , ? , ?)', (user_id, course_id, role))

    

    
conn.commit()
conn.close()

 
                  