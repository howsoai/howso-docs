"""Update notebook documentation pages to ensure cells are formatted with the correct cell type and mime type."""
import json
from pathlib import Path

for p in Path(__file__).parent.joinpath("source").glob("**/*.ipynb"):
    with open(p, encoding="utf8") as f:
        nb = json.load(f)

    modified = False
    for cell in nb["cells"]:
        cell_type = cell.get("cell_type")

        if cell_type == "markdown":
            cell["cell_type"] = "raw"
            modified = True
        elif cell_type != "raw":
            continue

        if not cell.get("metadata"):
            cell["metadata"] = {}

        if cell["metadata"].get("raw_mimetype") != "text/restructuredtext":
            cell["metadata"]["raw_mimetype"] = "text/restructuredtext"
            modified = True

    if modified:
        with p.open("w") as f:
            json.dump(nb, f, indent=1)
