import json
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

# Get JSON data
with open("news_url.json", "r", encoding="utf-8") as url_lists:
    article = json.load(url_lists)


# route to create main page
@app.route('/')
def main():
    return render_template('main.html')

# route to create BBC page
@app.route("/BBC")
def get_bbc():
    """
        Function to get data of BBC rss page.
        Created an empty list to add all the datas
        and rendered it
    """
    feeds = feedparser.parse(article["BBC"])
    all_the_news = []
    for content in feeds['entries']:
        all_the_news.append(content)
    return render_template('bbc.html', all_the_news=all_the_news)

# route to create CNN page
@app.route("/CNN")
def show_cnn():
        """
        Function to get data of CNN rss page.
        Same with the function of BBC
        """
        feeds = feedparser.parse(article["CNN"])
        all_the_news = []
        for content in feeds['entries']:
            all_the_news.append(content)
        return render_template('cnn.html', all_the_news=all_the_news)

        