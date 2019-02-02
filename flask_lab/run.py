from flask import Flask

import pymongo

app = Flask(__name__)

x = 0#record the times getting "hello"
myclient = pymongo.MongoClient()#create a client
mydb = myclient["timesdb"]#create a db
mycol = mydb["sites"]#create site
mydict = { "name": "times", "times": str(x)}
# make sure "times" is 0
if mycol.find_one({"name":"times"}) is  None: 
    mycol.insert_one(mydict) 
    print('create a new collection')
else:
    change = mycol.find_one({"name":"times"})
    change["times"] = str(0)  
    mycol.update({"name":"times"}, change)
    print('set it to 0\n')
    results = mycol.find({'name': 'times'})
    for result in results:
        print(result)

@app.route('/hello')
def hello_world():
    global x
    x = x + 1
    results = mycol.find({'name': 'times'})
    for result in results:
        print(result)
    condition = {"name":"times"}
    change = mycol.find_one(condition)
    change["times"] = str(x)
    mycol.update(condition, change)#update is neccessary 
    return "Hello World!" 

@app.route('/times')
def times():
    result = mycol.find_one({"name":"times"})#it returns a dictionary
    #index = str(result).find("'times':") + 10 
    #res = str(result)[index: index + 1]
    res = result["times"]
    return "You have sent hello " + str(res) + " times"

if __name__ == '__main__':
    app.run(port = 3000)
