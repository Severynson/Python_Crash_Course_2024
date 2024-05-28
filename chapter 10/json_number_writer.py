from pathlib import Path
import json

numbers = [6, 2, 8, 5, 1, 6]
path = Path.cwd() / "chapter 10" / "numbers.json"
contents = json.dumps(numbers)
path.write_text(contents)
