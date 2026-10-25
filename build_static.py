"""Render the Flask app into static files for GitHub Pages."""
from pathlib import Path

from app import app

OUT = Path("site")


def build():
    OUT.mkdir(exist_ok=True)
    client = app.test_client()
    (OUT / "index.html").write_bytes(client.get("/").data)
    (OUT / "health.json").write_bytes(client.get("/health").data)


if __name__ == "__main__":
    build()
    print(f"Static site written to {OUT}/")
