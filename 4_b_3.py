from pymongo import MongoClient

try:
    connection=MongoClient('localhost',27017)
except:
    print("Error in connection")

db=connection.aditya
collection=db.movies

n=int(input("enter the value of n : "))

# 1 actors in max movies
result1=collection.aggregate([
    {"$unwind":"$cast"},
    {"$group":{"_id":{"actor":"$cast"},"no_of_movies":{"$sum":1}}},
    {"$sort":{"no_of_movies":-1}},
    {"$limit":n}
])
for i in result1:
    print(i)

# 2 who starred in max movies in given year

year=input("enter the year : ")
result2=collection.aggregate([
    {"$match":{"year.$numberInt":year}},
    {"$unwind":"$cast"},
    {"$group":{"_id":{"actor":"$cast"},"no_of_movies":{"$sum":1}}},
    {"$sort":{"no_of_movies":-1}},
    {"$limit":n}
])
for i in result2:
    print(i)

# 3 for given genre

genre=input("enter the genre: ")
result3=collection.aggregate([
    {"$unwind":"$cast"},
    {"$match":{"genres":genre}},
    {"$group":{"_id":{"actor":"$cast"},"no_of_movies":{"$sum":1}}},
    {"$sort":{"no_of_movies":-1}},
    {"$limit":n}
])
for i in result3:
    print(i)