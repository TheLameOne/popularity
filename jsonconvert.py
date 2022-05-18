import sqlite3
import json

file = open('dummydata.json','w')
def get_all_users( json_str = False ):
    conn = sqlite3.connect('datacopy.sqlite')
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT * from account where trust > 1 order by followers desc
    ''').fetchall()

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

file.write(get_all_users( json_str = True ))
file.close()