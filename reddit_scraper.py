
import datetime as dt

import praw
import pandas as pd

#client id: TMHoskmwUtftxK04n7vkjA
#secret:	-ouUXyoIlfeJtBflvSF6KivTYGh0EQ

# Replace with your credentials
reddit = praw.Reddit(client_id='TMHoskmwUtftxK04n7vkjA',
                     client_secret='-ouUXyoIlfeJtBflvSF6KivTYGh0EQ',
                     user_agent='Additional-Cold430')

# Target subreddit and keyword
subreddit_name = "TwoXChromosomes"
keyword = "tradwife"

# How many comments to check
limit = 500

# Fetch and filter comments
subreddit = reddit.subreddit(subreddit_name)

matching_submissions = []

for submission in reddit.subreddit('TwoXChromosomes').search('tradwife', limit=50, sort='new'):
    matching_submissions.append(submission)

all_data = []
for submission in matching_submissions:
    submission.comments.replace_more(limit=0)  # Flatten comment tree
    for comment in submission.comments.list():
        if 'tradwife' in comment.body.lower():
            all_data.append({
                'type': 'comment',
                'id': comment.id,
                'post_id': submission.id,
                'created_utc': comment.created_utc,
                'author': str(comment.author),
                'body': comment.body,
                'score': comment.score,
                'permalink': f"https://www.reddit.com{comment.permalink}"
            })
    
    # Include the post itself
    if 'tradwife' in submission.title.lower() or 'tradwife' in submission.selftext.lower():
        all_data.append({
            'type': 'submission',
            'id': submission.id,
            'post_id': submission.id,
            'created_utc': submission.created_utc,
            'author': str(submission.author),
            'body': f"{submission.title}\n\n{submission.selftext}",
            'score': submission.score,
            'permalink': f"https://www.reddit.com{submission.permalink}"
        })


print(" Scanning for keyword matches...")
for comment in subreddit.comments(limit=10):
    print(comment.body)

# Convert to DataFrame
#df = pd.DataFrame(comments_data)
df = pd.DataFrame(all_data)

if not df.empty:
    # Optional: format timestamp
    if 'created_utc' in df.columns:
        df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')

    # Save to CSV
    df.to_csv('tradwife_live_comments.csv', index=False)
    print(f"✅ Saved {len(df)} comments to tradwife_live_comments.csv")
else:
    print(" No matching posts found.")
