from flask import Flask, jsonify

from main import greet

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
