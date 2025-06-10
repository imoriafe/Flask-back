print("Running run.py...")

from app import create_app

print("Creating Flask app...")
app = create_app()

print("Starting app...")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
