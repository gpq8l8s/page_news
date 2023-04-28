import json
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

with open("news_url.json", "r", encoding="utf-8") as url_lists:
    article = json.load(url_lists)

# HOME
@app.route('/')
def main():
    return render_template('main.html')

# BBC
@app.route("/BBC")
def get_bbc():
        feeds = feedparser.parse(article["BBC"])
        all_the_news = []
        for content in feeds['entries']:
            all_the_news.append(content)
        return render_template('bbc.html', all_the_news=all_the_news)

# CNN
@app.route("/CNN")
def show_cnn():
        """
        
        """
        feeds = feedparser.parse(article["CNN"])
        all_the_news = []
        for content in feeds['entries']:
            all_the_news.append(content)
        return render_template('cnn.html', all_the_news=all_the_news)

        