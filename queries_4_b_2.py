from pymongo import MongoClient

try:
    connection=MongoClient('localhost',27017)
except:
    print("Error in connection")

db=connection.aditya
collection=db.movies

n=int(input("enter the value of n: "))

# 4.2.1) find n directors with max movies
result=db.movies.aggregate([
    {"$unwind":"$directors"},
    {"$group":{"_id":{"director":"$directors"},"num_of_movies":{"$sum":1}}},
    {"$sort":{"num_of_movies":-1}},
    {"$limit":n}
])
for i in result:
    print(i)

# 4.2.2) who created the max num of movies in given year

year=input("enter the year: ")
result1=db.movies.aggregate([
    {"$unwind":"$directors"},
    {"$match":{"year.$numberInt":year}},
    {"$group":{"_id":{"director":"$directors"},"num_of_movies":{"$sum":1}}},
    {"$sort":{"num_of_movies":-1}},
    {"$limit":n}
])
for i in result1:
    print(i)

# 4.2.3) for given genre

genre=input("enter the genre: ")
result2=db.movies.aggregate([
    {"$unwind":"$directors"},
    {"$match":{"genres":genre}},
    {"$group":{"_id":{"director":"$directors"},"num_of_movies":{"$sum":1}}},
    {"$sort":{"num_of_movies":-1}},
    {"$limit":n}
])
for i in result2:
    print(i)

