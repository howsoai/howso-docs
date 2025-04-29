import json
from pathlib import Path

for p in Path(__file__).parent.glob("**/*.ipynb"):
    with open(p) as f:
        nb = json.load(f)

    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        cell["cell_type"] = "raw"
        if not cell.get("metadata"):
            cell["metadata"] = {}
        cell["metadata"]["raw_mimetype"] = "text/restructuredtext"

    with open(p, "w") as f:
        json.dump(nb, f)
