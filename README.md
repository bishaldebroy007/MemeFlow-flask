# MemeFlow

A simple and elegant Flask web application that fetches and displays random memes from Reddit using the [Meme API](https://github.com/D3vd/Meme_Api).

## Features

- Random Memes - Each page load fetches a fresh meme from Reddit.
- Subreddit Badge - Shows which subreddit the meme came from.
- Modern UI - Glassmorphism design with smooth hover effects.
- One-Click Refresh - "Next Meme" button reloads for a new meme instantly.
- Error Handling - Graceful fallback image if API fails.

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML5, CSS3, Font Awesome (icons)
- External API: [Meme API](https://meme-api.com/gimme)

## Project Structure

```
meme-project/
├── meme_flask.py # Flask application
├── templates/
│ └── index.html # Main HTML template
├── README.md
└── requirements.txt # (see below)
```

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/meme-flow.git
   cd meme-flow
   ```
2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install flask requests
   ```
   Or, create a requirements.txt file:

```bash
Flask==2.3.3
requests==2.31.0
```

## Preview

<img width="1228" height="862" alt="image" src="https://github.com/user-attachments/assets/4fc2e387-dc74-49a9-9e2a-5f6b3bfcf232" />

<img width="1013" height="898" alt="image" src="https://github.com/user-attachments/assets/84ad43ff-7029-45b8-977e-3d4e2741e3fe" />



Then run `pip install -r requirements.txt`

4. Run the application

```bash
python meme_flask.py
```
