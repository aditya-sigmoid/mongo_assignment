
 #  insert data in movies

from pymongo import MongoClient


try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db=connection.aditya
collection=db.movies

my_data={
    "plot" : "Three men hammer on an anvil ",
    "genres" : [
        "Short"
    ],
    "runtime" : {
        "$numberInt" : "1"
    },
    "cast" : [
        "Charles Kayser",
        "John Ott"
    ],
    "num_mflix_comments" : {
        "$numberInt" : "1"
    },
    "title" : "Blacksmith Scene",
    "fullplot" : "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
    "countries" : [
        "USA"
    ],
    "released" : {
        "$date" : {
            "$numberLong" : "-2418768000000"
        }
    },
    "directors" : [
        "William K.L. Dickson"
    ],
    "rated" : "UNRATED",
    "awards" : {
        "wins" : {
            "$numberInt" : "1"
        },
        "nominations" : {
            "$numberInt" : "0"
        },
        "text" : "1 win."
    },
    "lastupdated" : "2015-08-26 00:03:50.133000000",
    "year" : {
        "$numberInt" : "1893"
    },
    "imdb" : {
        "rating" : {
            "$numberDouble" : "6.3"
        },
        "votes" : {
            "$numberInt" : "1189"
        },
        "id" : {
            "$numberInt" : "5"
        }
    },
    "type" : "movie",
    "tomatoes" : {
        "viewer" : {
            "rating" : {
                "$numberInt" : "2"
            },
            "numReviews" : {
                "$numberInt" : "184"
            },
            "meter" : {
                "$numberInt" : "32"
            }
        },
        "lastUpdated" : {
            "$date" : {
                "$numberLong" : "1435516449000"
            }
        }
    }
}

received_id=collection.insert_one(my_data)
print("data insert with record id : ",received_id)





from pymongo import MongoClient

try:
    connection = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db=connection.aditya
collection=db.theaters

my_data={
    "theaterId" : {
        "$numberInt" : "1000"
    },
    "location" : {
        "address" : {
            "street1" : "340 Market",
            "city" : "Bloomington",
            "state" : "MN",
            "zipcode" : "55425"
        },
        "geo" : {
            "type" : "Point",
            "coordinates" : [
                {
                    "$numberDouble" : "-93.255"
                },
                {
                    "$numberDouble" : "44.866"
                }
            ]
        }
    }


}
required_id=collection.insert_one(my_data)
print(required_id)





