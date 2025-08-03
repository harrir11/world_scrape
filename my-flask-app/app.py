import os
import io
import praw
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

os.makedirs("static", exist_ok=True)
  # use a non-interactive backend

# PRAW setup
reddit = praw.Reddit(
    client_id='TMHoskmwUtftxK04n7vkjA',
    client_secret='-ouUXyoIlfeJtBflvSF6KivTYGh0EQ',
    user_agent='Additional-Cold430'
)
send_file('/')
def home():
    return "Flask is running! Use POST /search with JSON."

@app.route('/search', methods=['POST'])
def search_reddit():
    data = request.json
    keyword = data.get("keyword", "").lower()
    subreddit_name = data.get("subreddit", "TwoXChromosomes")

    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    all_data = []
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.search(keyword, limit=50, sort='new'):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if keyword in comment.body.lower():
                all_data.append({
                    'type': 'comment',
                    'created_utc': comment.created_utc
                })

        if keyword in submission.title.lower() or keyword in submission.selftext.lower():
            all_data.append({
                'type': 'submission',
                'created_utc': submission.created_utc
            })

    df = pd.DataFrame(all_data)

    if df.empty:
        return jsonify({"message": "No results found"}), 200

    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    df['month'] = df['created_utc'].dt.to_period('M').astype(str)

    counts = df.groupby('month').size()

    # Create a simple bar chart
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar')
    plt.title(f"Mentions of '{keyword}' in r/{subreddit_name}")
    plt.xlabel("Month")
    plt.ylabel("Number of Mentions")
    plt.xticks(rotation=45)
    plt.tight_layout()

    img_path = os.path.join('static', 'keyword_graph.png')
    plt.savefig(img_path)
    plt.close()

    # Send the image back
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
