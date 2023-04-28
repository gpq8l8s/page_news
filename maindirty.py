import json
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

with open("news_url.json", "r", encoding="utf-8") as url_lists:
    article = json.load(url_lists)

# HOME
# menu = """<html>
#             <body>
#                 <div class="menu_container>
#                     <div class="menu_home">
#                         <div class="menu bbcmenu"><a href="/BBC"><h1>BBC News</h1></a></div>
#                         <div class="menu cnnmenu"><a href="/CNN"><h1>CNN News</h1></a></div>
#                     </div>
#                 </div>
#             </body>
#         </html>"""
# css_home = """<html>
#         <style>
#             * {
#                 margin: 0;
#                 padding: 0;
#                 color: #000;
#             }
#             /menu_container
#             .menu_home {
#                 position: absolute;
#                 top: 50%;
#                 left: 50%;
#                 transform: translate(-50%, -50%);
#             }
#             .menu_home > menu {
            
#             }
#             .menu_home > menu > a {
#                 text-decoration: none;
#                 margin: 
#             }
#             .menu_home > menu > a > h1 {
#                 margin-bottom: 30px;
#             }
#         </style>
#     </html>"""

# @app.route("/")
# def home():
#     return """<html>
#         <head>
#             {0}
#         </head>
#         <body>
#             {1}
#         </body>
#     </html>""".format(css_home, menu)
@app.route('/')

# BBC
@app.route("/BBC")
def get_news():
        feeds = feedparser.parse(article["BBC"])
        # loop
        all_the_news = []
        for content in feeds['entries']:
            title = content.get('title')
            title_detail = content.get('title_detail')
            # summary = content.get('summary')
            link = content.get('link')
            published = content.get('published')
            infos = """<a href='{3}'>
                <h2>{0}</h2>
                <p>{1}</p>
                <p>{2}</p>
                <p>{4}</p>
            </a>""".format(title, title_detail, summary, link, published)
            all_the_news.append(infos)
            all_the_news_line = "\n".join(all_the_news)
            css = """<style>
                a {text-decoration: none; list-style: none; color:#000;}
            </style>"""
        return """<html>
            <head>{0}</head>
            <body>
                <h1>BBC News</h1>
                {1}
            </body>
        </html>""".format(css, all_the_news_line)

# CNN
@app.route("/CNN")
def show_cnn():
        feeds = feedparser.parse(article["CNN"])
        all_the_news = []

        # Take all the elements and create HTML
        for content in feeds['entries']:
            title = content.get('title')
            title_detail = content.get('title_detail')
            description = content.get('description')
            published = content.get('published')
            link = content.get('link')
            news = """<html>
                <body>
                    <a href="{4}">
                        <h2>{0}</h2>
                        <p>{1}</p>
                        <p>{2}</p>
                        <p>{3}</p>
                    </a>
                </body>
            </html>""".format(title, title_detail, description, published, link)
            all_the_news.append(news)
            all_the_news_line = "\n".join(all_the_news)

            # CSS
            css = """<style>
                a{}
            </style>"""
        return """<html>
            <body>
                <h1>DNN News</h1>
                {0}
            </body>
        </html>""".format(all_the_news_line)


# @app.route("/")
# def get_news():
#     feed = feedparser.parse(newsBBC)
#     article = feed['entries'][0]
#     return """<html>
#             <body>
#                 <p>{0}<br/></p>
#                 <p>{1}<br/></p>
#                 <p>{2}<br/></p>
#             </body>
#         </html>""".format(article.get("title"),article.get("published"), article.get("summary"))
