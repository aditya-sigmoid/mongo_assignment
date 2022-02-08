from pymongo import MongoClient

try:
    connection=MongoClient('localhost',27017)
except:
    print("Error in connection")

db=connection.aditya
collection=db.movies

n=int(input("enter the value of n : "))

result=collection.aggregate([
    {"$unwind":"$genres"},
    {"$project":{"_id":0,"genre":"$genres"}}
])

# to get the distinct genre storing it in a set
distinct=set()
for i in result:
    distinct.add(i.get("genre"))


# iterating through the set to get highest rating movies in each genre
for genre in distinct:
    print("The genre of the movie is : ",genre)

    result=collection.find({"genres":genre },{"_id": 0, "title": 1, "imdb.rating": 1}).sort("imdb.rating" ,-1).limit(n)
    for movie in result:
        print(movie)
    print()
