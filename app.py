import datetime

from flask import Flask, jsonify

from main import greet

app = Flask(__name__)
VERSION = "1.1.0"

PAGE = """<!doctype html>
<html lang="uk">
<head>
  <meta charset="utf-8">
  <title>DevOps Lab</title>
</head>
<body>
  <h1>{message}</h1>
  <p>Застосунок автоматично перевіряється та розгортається через GitHub Actions.</p>
</body>
</html>
"""


@app.route("/")
def index():
    return PAGE.format(message=greet("DevOps"))


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/version")
def version():
    return jsonify(version=VERSION)


if __name__ == "__main__":
    app.run(debug=True)
