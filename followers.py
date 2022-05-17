import instaloader
import sqlite3
L = instaloader.Instaloader()

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
cur.execute('''SELECT username FROM account order by trust DESC''')
data = cur.fetchall()
i = 0
for i in data:
   username = i[0]
   profile = instaloader.Profile.from_username(L.context, username)
   followers = profile.followers
   cur.execute('UPDATE account SET followers = ? WHERE username = ?',(followers,username))
   print("Updated followers for {} : {}",username,followers)
   i =+ 1
   if(i%10 == 0):
       conn.commit()
conn.commit()