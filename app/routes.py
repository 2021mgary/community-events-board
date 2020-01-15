import os
from app import app
from flask import render_template, request, redirect


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'events'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:4wmJFdZIxF9JQ0Rg@cluster0-frdoa.mongodb.net/events?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    # connect to the database
    collection = mongo.db.events
    # query to the database to get all the Events
    # store those events as a list of dictionaries called events
    events = list(collection.find({}))
    # print the events
    for event in events:
        print(event["event_name"])
        print(event["event_date"])
        print(event["event_type"])
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": "test", "event_date": "today", "event_type": "category"})
    # return a message to the user
    return "you added an event to the database"

#add methos to this route -- get, post data
@app.route('/results', methods=["get", "post"])

def results():
    # store user info from the form
    userinfo=dict(request.form)
    print(userinfo)
    # get the event name and the event date and store them
    event_name = userinfo["event_name"]
    event_date = userinfo["event_date"]
    event_type = userinfo["event_type"]
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": event_name, "event_date": event_date, "event_type": event_type})
    # return a message to the user
    return redirect("/index")

@app.route('/secret')
def secret():
    # connect to the database
    collection = mongo.db.events
    # dete everything from the database
    # invoke the delete_many method to the collection
    collection.delete_many({})
    return redirect('/index')

@app.route('/education')
def education():
    collection = mongo.db.events
    education = list(collection.find({"event_type": "education"}))
    for item in education:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('education.html', events = education)

@app.route('/social')
def social():
    collection = mongo.db.events
    social = list(collection.find({"event_type": "social"}))
    for item in social:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('social.html', events = social)

@app.route('/service')
def service():
    collection = mongo.db.events
    service = list(collection.find({"event_type": "service"}))
    for item in service:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('service.html', events = service)

@app.route('/sporting')
def sporting():
    collection = mongo.db.events
    sporting = list(collection.find({"event_type": "sporting"}))
    for item in sporting:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('sporting.html', events = sporting)


@app.route('/business')
def business():
    collection = mongo.db.events
    business = list(collection.find({"event_type": "business"}))
    for item in business:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('business.html', events = business)

@app.route('/other')
def other():
    collection = mongo.db.events
    other = list(collection.find({"event_type": "other"}))
    for item in other:
        print(item["event_name"], item["event_date"], item["event_type"])
    return render_template('other.html', events = other)
