# ----------------------------------------------------------------------
# Step 1: Import all necessary modules and create Flask+PyMongo app
# ---------------------------------------------------------------------- 
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app)

# ----------------------------------------------------------------------
# Step 3: Set up routes
# ---------------------------------------------------------------------- 

# Route 1: Scrape and store data in MongoDB
@app.route("/")
def index():
    try:
        mars_data = mongo.db.mars.find_one()
        print("happy panda")
    except:
        mongo.db.mars.insert_one(scrape_mars.scrape())
        mars_data = mongo.db.mars.find_one()
        print("exception whee")
    return render_template("index.html", mars=mars_data)
    
# Route 2: Scrape and store data in MongoDB
@app.route("/scrape")
def scrape():
    try:
        mongo.db.mars.find_one()
        mongo.db.mars.delete_one()
        mongo.db.mars.insert_one(scrape_mars.scrape())
    except:
        mongo.db.mars.insert_one(scrape_mars.scrape())
    
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)