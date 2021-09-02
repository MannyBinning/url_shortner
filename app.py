import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, url_for)
from flask_pymongo import PyMongo
import random
import string

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
# Form Submission method
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        finding_url = mongo.db.urls.find_one(
            {"original_url": request.form.get("original_url")})
        short_url = shorten_url()
        if finding_url:
            return redirect(url_for("display_short_url",url=finding_url["short_code"]))
        new_urls = {
            "original_url": request.form.get("original_url"),
            "new_url": "short-li.herokuapp.com/"+short_url,
            "short_code": short_url
        }
        mongo.db.urls.insert_one(new_urls)
        return redirect(url_for("display_short_url", url=short_url))      
    return render_template("index.html")


# Random letter generator method
def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        short_url = mongo.db.urls.find_one(
            {"short_code": request.form.get("short_code")})
        if not short_url:
            return rand_letters


# to display new ur for the user
@app.route("/display/<url>")
def display_short_url(url):
    original_urls = mongo.db.urls.find().sort("original_url", 1)
    new_urls = mongo.db.urls.find().sort("new_url", 1)
    return render_template("short_url.html", short_url_display=url, original_urls=original_urls, new_urls=new_urls)


# Redirect user to the original URL
@app.route("/<short_url>")
def redirection(short_url):
    real_url = mongo.db.urls.find_one({"short_code": short_url})
    if real_url:
        return redirect(real_url["original_url"])
    else:
        return "url not available"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)