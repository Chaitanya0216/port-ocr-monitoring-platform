from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "project": "Port OCR Monitoring Platform",
        "status": "running",
        "message": "Backend is working successfully!"
    }


if __name__ == "__main__":
    app.run(debug=True)