import pymongo

def search():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.gter
    collection = db.data

    for result in collection.find():
        print(result)


if __name__ == "__main__":
    search()
