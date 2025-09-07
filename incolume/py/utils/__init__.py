"""incolumepy.utils module."""

from pathlib import Path

try:
    import tomllib as tomli  # type: ignore[import]
except ImportError:
    import tomli  # type: ignore[import]

confproject = Path(__file__).parents[3] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"

with confproject.open("rb") as f:
    versionfile.write_text(tomli.load(f)["project"]["version"] + "\n")

__version__ = versionfile.read_text().strip()
__title__ = "incolume.py.utils"
