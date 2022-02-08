from datetime import datetime

from pymongo import MongoClient
from bson import ObjectId

try:
    connection=MongoClient('localhost',27017)
except:
    print("Error in connect")

db=connection.aditya
collection=db.comments



# a.i) find top 10 users who made the maximum no of comments

top_10_user = collection.aggregate([

  {"$group": {"_id": {"email": "$email"}, "name": {"$first": "$name"}, "total_comment": {"$sum": 1}}},
    {"$sort": {"total_comment": -1}},
   {"$project": {"_id": 0, "name": 1, "total_comment": 1}},
  {"$limit": 10}
  ])
for user in top_10_user:
    print(user)


#  a.ii) find top 10 movies with most comments

top_10= collection.aggregate([

    {"$group": {"_id": { "movies_id": "$movie_id"},"total_comment":{"$sum":1}}},
    {"$sort": {"total_comment": -1}},
    {"$project": {"movies_id": 1,"total_comment":1}},
    {"$limit": 10}
])

mov=list(top_10)
mov_id=[]
for i in range(0,len(mov)):
    oid=mov[i]['_id']['movies_id']['$oid']
    obj=ObjectId(oid)
    mov_id.append(obj)

collection1=db.movies

for id1 in mov_id:
    val=collection1.find({"_id":id1},{"_id":0,"title":1})
    for title in val:
        print(title)






# a.iii) given a year find the total no of comments created each month in that year

year=input("enter the year : ")

dic= {  "01":0,"02":0,  "03": 0, "04": 0,"05": 0,"06": 0,"07": 0,"08": 0, "09": 0,"10": 0,"11": 0,"12": 0}
for i in collection.find():
    dte = i['date']['$date']['$numberLong']
    datetime_obj = datetime.fromtimestamp(float(dte)/1e3)
    date = datetime_obj.date()
    x = str(date)
    yr = x[0:4]
    mo = x[5:7]
    if(yr==year):
        dic[mo] +=1

for k,v in dic.items():
    print(k,"->",v)