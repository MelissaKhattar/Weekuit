# Weekuit

A weekly dashboard of things to do in Utrecht and across the Netherlands: culture, active things, concerts, festivals and popular deals.

Live version: https://claude.ai/artifact/5dkG9kLRJBXPv81odvwGwf (likes are shared and kept there).

## What it does
- Filter by place (Utrecht or rest of NL), type, and budget.
- Like or pass on events. After 5 votes it hides what you'd likely skip; after 15 it gets strict.
- Prices marked ~ are estimates.

## Files
- `src/template.html`: the page, with events injected at the `/*EVENTS*/` marker.
- `data/events-YYYY-wNN.json`: one file per week.
- `SOURCES.md`: where events come from.
- `build.py`: builds `index.html` from the template and the newest week. Opened as a plain file, votes are saved in the browser only.

## Update
Every Sunday a routine collects next week's events, adds a data file and republishes the live page.

```
python3 build.py
```
