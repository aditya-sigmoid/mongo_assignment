
from pymongo import MongoClient
try:
    connection=MongoClient('localhost',27017)
except:
    print('Error in connection')

db=connection.aditya

collection=db.movies

n=int(input("enter the value of n : "))

# b.i.1) find top n movies with highest imdb rating

result=collection.find({"imdb.rating": {"$ne":""} },{"_id": 0, "title": 1, "imdb.rating": 1}).sort("imdb.rating" ,-1).limit(n)
for movie in result:
    print(movie)

# b.i.2) with the highest imdb rating in a year

year=input("enter the year : ")
answer=collection.aggregate([
    {"$match":{"year.$numberInt":year}},
    {"$project":{"_id":0,"movies":"$title","rating":"$imdb.rating"}},
    {"$sort":{"rating":-1}},
    {"$limit":n}
])
for value in answer:
    print(value)



# b.i.3) with no of votes>1000

###  not showing the answer dont know why ...

result1=collection.aggregate([
    {"$project":{"_id":0,"vote":{"$convert":{"input":"$imdb.votes","to":"int","onError":0}},"rating":"$imdb.rating","title":"$title"}},
    {"$match":{"vote": {"$gt":1000}}},
    {"$project":{"_id":0,"title":1,"rating":1,"votes":1}},
    {"$sort":{"rating":-1}},
    {"$limit":n}
])
for movie in result1:
    print(movie)


# b.i.4) with title matching a given pattern sorted by highest tomatoes ratings

pattern=input("enter the pattern to search ")
result2=db.movies.find({"title":{"$regex":pattern}},{"_id":0,"title":1,"tomatoes.viewer.rating":1}).sort("tomatoes.viewer.rating",-1).limit(n)
for i in result2:
    print(i)

