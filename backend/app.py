from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def load_articles(filename="/workspaces/mini-search-engine/backend/data/articles.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def search_articles(query, articles):
    docs = [article['content'] for article in articles]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    relevant_indices = cosine_similarities.argsort()[-10:][::-1]
    return [articles[i] for i in relevant_indices]

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    articles = load_articles()
    results = search_articles(query, articles)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)


