from pymongo import MongoClient

try:
    connection=MongoClient('localhost',27017)
except:
    print("Error in connection")

db=connection.aditya
collection=db.theaters

# 1. Top 10 cities with  maximum number of theatres

res = collection.aggregate([
        {"$group": {"_id": "$location.address.city","total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 10}
])
for i in res:
    print(i)

# 2. theaters near the given coordinates

dic = {}
coord=['-91.22265','45.91266']
for i in collection.find():
    cord_data = i['location']['geo']['coordinates']
    x = float(coord[0]) - float(cord_data[0]['$numberDouble'])
    y = float(coord[1]) - float(cord_data[1]['$numberDouble'])
    x = round(x * x + y * y, 5)
    if dic.get(x):
        dic[x].append(i['theaterId'])
    else:
        dic[x] = []
        dic[x].append(i['theaterId'])
a = dict(sorted(dic.items()))
ans = []
for k, v in a.items():
    if len(ans) + len(v) > 10:
        x = 10 - len(ans)
        ans += v[0:x]
    else:
        ans += v
    if len(ans) >= 10:
        break
for i in ans:
    print(i)
