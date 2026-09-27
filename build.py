"""Build index.html from src/template.html and the newest data/events-*.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
data = sorted((root / "data").glob("events-*.json"))[-1]
events = json.loads(data.read_text())
page = (root / "src" / "template.html").read_text().replace("/*EVENTS*/", json.dumps(events, ensure_ascii=False))
(root / "index.html").write_text(
    '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
    + page + "</body></html>\n")
print(f"Built index.html from {data.name} ({len(events['events'])} events)")
