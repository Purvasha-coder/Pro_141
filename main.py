from flask import Flask, jsonify
import csv

all_articles = []
liked_articles = []
unliked_articles = []

with open('articles.csv', 'r', encoding = "utf-8") as f:
    reader = csv.reader(f)
    article_data = list(reader)
    all_articles = article_data[1:]

app = Flask(__name__)

@app.route('/article-data')
def home():
    return jsonify({
        'data': all_articles[0],
        'message': 'successful'
    }), 404

@app.route('/liked-articles', methods = ['POST'])
def liked():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'message': 'successful'
    }), 404

@app.route('/unliked_articles', methods = ['POST'])
def unliked():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        'message': 'successful'
    }), 404

if __name__ == '__main__':
    app.run()