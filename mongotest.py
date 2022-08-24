import pymongo

client = pymongo.MongoClient("mongodb+srv://Shivam:Shivam123@cluster0.yfcwyz1.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d = {
    "name": "Shivam",
    "email": "saxena958@gmail.com",
    "surname": "Saxena"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
