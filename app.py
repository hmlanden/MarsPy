# ----------------------------------------------------------------------
# Step 1: Import all necessary modules and create Flask app
# ---------------------------------------------------------------------- 
from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# ----------------------------------------------------------------------
# Step 2: Set up Pymongo DB connection
# ---------------------------------------------------------------------- 
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.mars

# ----------------------------------------------------------------------
# Step 3: Set up routes
# ---------------------------------------------------------------------- 

# Route 1: Scrape and store data in MongoDB
@app.route("/")
def index():
    mars_data = db.collection.find()
    return render_template("index.html", mars_data=mars_data)
    
# Route 2: Scrape and store data in MongoDB
@app.route("/scrape")
def scrape():
    import scrape_mars as mars
    db.collection.insert(mars.scrape())

if __name__ == "__main__":
    app.run(debug=True)