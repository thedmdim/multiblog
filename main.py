import os, glob, mistune
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

SECRET_KEY = "51298bfcfcc5a83ab27a8f4df4234ffa3890f404"
POSTS = os.path.join(app.root_path, "posts")

app.config.from_object(__name__)

@app.route("/")
@app.route("/<string:author>/")
def article_list(author=None):
    if author:
        files = glob.glob(os.path.join(app.config["POSTS"], author, "*.md"))
    else:
        files = glob.glob(os.path.join(app.config["POSTS"], "*", "*.md"))

    posts = []
    for file in files:
        date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%d.%m.%Y')
        title = open(file).readline().replace("#","").lstrip()

        path = file.split("\\")

        author = path[-2]
        article = path[-1].replace(".md","")
        href = f"/{author}/{article}"

        posts.append({"date": date, "author":author, "title":title, "href":href})


    return render_template("index.html", posts=posts)

@app.route("/<string:author>/<string:article>")
def author_atricles(author=None, article=None):
    if author and article:
        print(os.path.join(app.config["POSTS"], author, article + '.md'))
        #article_html = markdown.markdown(open(os.path.join(app.config["POSTS"], author, article+'.md')).read())
        article_html = mistune.html(open(os.path.join(app.config["POSTS"], author, article + '.md')).read())
        return render_template("post.html", article=article_html)
