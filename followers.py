import instaloader
import sqlite3
L = instaloader.Instaloader()

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
cur.execute('''SELECT username FROM account where followers = 0 order by trust DESC''')
data = cur.fetchall()
count = 0
for i in data:
   username = i[0]
   try:
       profile = instaloader.Profile.from_username(L.context, username)
   except:
       continue
   followers = profile.followers
   if(followers == 0):
       cur.execute('UPDATE account SET followers = ? WHERE username = ?',(-1,username))
   else:
       cur.execute('UPDATE account SET followers = ? WHERE username = ?',(followers,username))
   print("Updated followers for {} : {}".format(username,followers))
   count += 1
   if(count%10 == 0):
       conn.commit()
conn.commit()