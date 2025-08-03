**Reddit Sentiment & Keyword Scraper** \n
   A Python-based Reddit scraper built with PRAW, Pandas, and Flask, designed to search for keywords across subreddits, extract post and comment metadata, and visualize posting trends over time. Built as part of an ongoing project to explore online discourse, cultural trends, and sentiment shifts.

**Features** \n
     Keyword-based search across specified subreddits
     Collects post metadata (title, date, score, etc.) and comment data
     Simple Flask frontend for keyword input
     Outputs a graph showing post volume over time (by month)
     Exportable CSV for further analysis (e.g., in Excel or Jupyter)
     Ready for sentiment analysis pipeline integration

**Tech Stack** \n
    Backend: Python, Flask, PRAW (Reddit API)
    Frontend: HTML (Flask templates), basic React (optional)
    Data Processing: Pandas, Matplotlib
    Deployment-ready: GitHub Pages for frontend or Flask app hosting via Render/Heroku

**Project Structure** \n
    php
    Copy
    Edit
    reddit-scraper/
    ├── app.py                  # Flask app logic
    ├── reddit_scraper.py       # Keyword scraping logic
    ├── templates/
    │   └── index.html          # Input form for keyword
    ├── static/
    │   └── output.png          # Graph image output
    ├── data/
    │   └── results.csv         # Collected Reddit data
    ├── requirements.txt
    └── README.md

**Setup Instructions** \n
Clone the repository:

    bash
    Copy
    Edit
    git clone https://github.com/yourusername/reddit-scraper.git
    cd reddit-scraper
    Create a virtual environment (optional but recommended)
    
    bash
    Copy
    Edit
    python3 -m venv venv
    source venv/bin/activate
    Install dependencies
    
    bash
    Copy
    Edit
    pip install -r requirements.txt
    Set up your Reddit API credentials
    
    Create a .env file (or export variables directly):
    
    ini
    Copy
    Edit
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    USER_AGENT=your_custom_user_agent
    Run the app
    
    bash
    Copy
    Edit
    flask run
    Visit the web interface
    
    cpp
    Copy
    Edit
    http://127.0.0.1:5000

**Example Use Case** \n
Search for the keyword "tradwife" in r/TwoXChromosomes to visualize how often the term appears over time. Useful for tracking cultural moments, misinformation trends, or subreddit activity.

**Roadmap** \n
 Add support for multiple keywords
 Integrate basic sentiment analysis (TextBlob or Vader)
 UI enhancements with React or Bootstrap
 Historical data via Pushshift or archive import
 Host via Render or GitHub Pages

**Contributing** \n
Pull requests welcome! For major changes, please open an issue first to discuss what you’d like to change.

**License** \n
MIT License

