from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_the_meme():
    url = "https://meme-api.com/gimme"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = json.loads(response.text)
        meme_large = data.get("url") or data["preview"][-2]
        subreddit = data.get("subreddit", "memes")
        return meme_large, subreddit
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return "https://via.placeholder.com/900x600/1e293b/cbd5e1?text=No+meme+available", "memes"

@app.route('/')
def index():
    meme_large, subreddit = get_the_meme()
    return render_template('index.html', meme_large=meme_large, subreddit=subreddit)


if __name__ == "__main__":
    app.run(debug=True)