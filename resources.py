import instaloader
import sqlite3
L = instaloader.Instaloader()
USER = "ganjediiiii"
PASSWORD = "harshvansh"
L.login(USER, PASSWORD)
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# sources = open('sources.txt', 'r')
# sourceslist = []
# for i in sources:
#     sourceslist.append(i[:-1])
# sources.close()

# fetched = open('fetched.txt', 'r')
# fetchedlist = []
# for i in fetched:
#     fetchedlist.append(i[:-1])
# fetched.close()

# fetched = open('fetched.txt', 'a')

# for i in sourceslist:
#     if i == 'end':
#         break
#     if i not in fetchedlist:
#         fetched.write(i + "\n")
#         break
#     else:
#         continue
# fetched.close()

i = 'abes_ec_confessions '

if(i == 'end'):
    print("all accounts already fetched")
    exit
else:
    account = i[:-1]
    # print(account)
    profile = instaloader.Profile.from_username(L.context,account)
    print("fetching followers of " + profile.username)
    followers = profile.get_followers()
    # print(followers)
    for follower in followers:
        username = follower.username
        try:
            cur.execute('''SELECT username FROM account WHERE username = ? ''' , (username, ))
            username_presence  = cur.fetchone()[0]
        except:
            username_presence  = 0
        if username_presence == 0 or username_presence is None:
            cur.execute('''INSERT OR IGNORE INTO account (username, trust, followers)
                VALUES ( ?, ?, ? )''', ( username, 0, 0 ) )
            print(username, ' - added to database')
        else:
            cur.execute('''SELECT trust FROM account WHERE username = ? ''' , (username, ))
            trust_value = cur.fetchone()[0]
            cur.execute('UPDATE account SET trust = ? WHERE username = ?',( trust_value + 1,username))
            print('Already EXISTS Updating Trust  to - ', trust_value + 1)

conn.commit()