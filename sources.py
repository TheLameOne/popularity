import instaloader
s = "abes"
L = instaloader.Instaloader()

USER = ""
PASSWORD = ""
L.login(USER, PASSWORD)

search = instaloader.TopSearchResults(L.context, s)
usernames  = search.get_prefixed_usernames()

file = open('sources.txt','w')
for username in usernames:
    file.write(username + '\n')

file.close()
