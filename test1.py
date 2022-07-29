import pymongo

client = pymongo.MongoClient("mongodb+srv://vibhanshu:vibhanshu7@cluster0.9tfj4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"vibhanshu",
    "email": "vibhanshu.vs7@gmail.com",
    "lname":"srivastava"
}

db1 = client["mongotest"]
coll=db1['test']
coll.insert_one(d)