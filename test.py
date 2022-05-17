fetched = open('fetched.txt', 'r')
fetchedlist = []
for i in fetched:
    fetchedlist.append(i[:-1])
if("harsh" not in fetchedlist):
    print("jnot")