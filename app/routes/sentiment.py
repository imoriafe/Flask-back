from flask import Blueprint, request, jsonify

sentiment_bp = Blueprint("sentiment", __name__)
@sentiment_bp.route("/")
def home():
    return jsonify({"message": "Welcome to your backend API!"})

@sentiment_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    text = text.lower()
    if "hate" in text or "dislike" in text:
        sentiment = "Negative"
    elif "love" in text or "amazing" in text:
        sentiment = "Positive"
    elif "maybe" in text or "ok" in text:
        sentiment = "Neutral"
    else:
        sentiment = "Neutral"

    return jsonify({
        "text": text,
        "sentiment": sentiment
    })
