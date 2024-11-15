import os
import sys

# Add different levels to sys.path
paths_to_add = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")),
]

for path in paths_to_add:
    if path not in sys.path:  # Avoid duplicate entries
        sys.path.insert(0, path)
