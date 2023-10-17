import json
data = Path("movies.json").read_text(encoding="utf-8")
movies = json.loads(data)

movies = json.loads(Path("movies.json").read_text(encoding="utf-8")
