Flask Sentiment Analysis API

This is a simple Fla backend API that analyzes sentiment from user text.

🔧 Endpoints

POST /register – Register a user (mock)
POST /predict – Predict sentiment of input text
Sentiment Logic

The /predict endpoint looks for keywords:

Keyword Found	Sentiment
"hate", "dislike"	Negative
"love", "amazing"	Positive
"maybe", "ok"	Neutral
Live URL

[Your Replit Live App] (https://bbae760f-41b5-4fc6-a153-9b8c940fd4ae-00-3nv2xamwjkast.picard.replit.dev)

 Tech Stack

Python 3.11
Flask
JSON (REST API)
Replit Deployment
✅ How to Run Locally

pip install flask
python app.py
