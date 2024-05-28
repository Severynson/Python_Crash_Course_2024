from pathlib import Path
import json

path = Path.cwd() / "chapter 10" / "numbers.json"
contents = path.read_text()
numbers = json.loads(contents)
print(f'Numbers from the file located by path: "{path}": {numbers}')
