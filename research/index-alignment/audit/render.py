"""Render both research PDFs from local Markdown. See RENDERING.md."""
import os
from pathlib import Path
import subprocess

if __name__ == "__main__":
    subprocess.run([os.environ.get("NODE_BINARY", "node"), str(Path(__file__).with_suffix(".mjs"))], check=True)
