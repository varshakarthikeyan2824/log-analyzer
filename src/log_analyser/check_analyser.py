import json
from pathlib import Path

from log_analyser.analyser import analyse_log

result = analyse_log(Path("data/messy.log"))
print(json.dumps(result, indent=2))
