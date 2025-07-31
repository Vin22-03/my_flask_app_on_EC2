from flask import Flask

print("✅ Starting Flask app...")  # Debug line

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Vin — Cloud in the making 🚀"

if __name__ == "__main__":
    print("⚙️ Running Flask now...")
    app.run(host="0.0.0.0", port=5000)
