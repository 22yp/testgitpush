import pymongo
client = pymongo.MongoClient("mongodb+srv://yashika:Shr9YEdv8CnAFdO8@cluster0.ys6z6js.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"yashika",
    "email":"yashika@gmail.com",
    "sirname":"puri"
}
d = {
    "name":"yashika",
    "email":"yashika@gmail.com",
    "sirname":"puri"
}
d = {
    "name":"yashika",
    "email":"yashika@gmail.com",
    "sirname":"puri"
}
d = {
    "name":"yashika",
    "email":"yashika@gmail.com",
    "sirname":"puri"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
