from  googlesearch import search

print("welcome to the search engine  tool")

query = input("what do you want to search on google?:")

for i in search(query,start=0,stop=6):
    print(i)
