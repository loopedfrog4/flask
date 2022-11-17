from flask import Flask, render_template, url_for, request
from pymongo import MongoClient
import pprint

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.userDB
itemCollection = db.users

for item in itemCollection.find({"username": "x@y.com"}):
   pprint.pprint(item)


@app.route('/', methods=['POST', 'GET'])
def Hello():
   if request.method == 'POST':
      taskContent = request.form['search'];
      return taskContent
   else:
      return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)