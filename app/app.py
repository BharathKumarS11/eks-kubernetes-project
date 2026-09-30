from flask import Flask
import os
import socket

app = Flask(__name__)

MESSAGE = os.getenv(
    "APP_MESSAGE",
    "Hello from Kubernetes on Amazon EKS!"
)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>EKS DevOps Application</title>
        </head>
        <body>
            <h1>{MESSAGE}</h1>
            <h2>Pod: {hostname}</h2>
            <p>Application running on Amazon EKS.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)