
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your backend API!"})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    return jsonify({"message": f"User {username} registered!"})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # Mock prediction logic
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
    
