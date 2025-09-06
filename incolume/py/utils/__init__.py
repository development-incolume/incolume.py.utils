"""incolumepy.utils module."""
from pathlib import Path
try:
    import toml
except ImportError:
    import tomli as toml  # type: ignore[import]

confproject = Path(__file__).parents[3] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"

versionfile.write_text(
    toml.load(confproject)["tool"]["poetry"]["version"] + "\n"
)

__version__ = versionfile.read_text().strip()
__title__ = "incolume.py.utils"
