#!/usr/bin/python
import os
import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

load_dotenv()
database_uri = os.environ["MONGODB_URI"]

def create_app():
    app = Flask(__name__)
    client = MongoClient(database_uri)
    app.db = client.microblog


    @app.route("/", methods=["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entries_with_date)

    return app