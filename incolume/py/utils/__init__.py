"""incolumepy.utils module."""
from pathlib import Path
import toml

confproject = Path(__file__).parents[3] / "pyproject.toml"
versionfile = Path(__file__).parent / "version.txt"

versionfile.write_text(
    toml.load(confproject)["tool"]["poetry"]["version"] + "\n"
)

__version__ = versionfile.read_text().strip()
__title__ = "incolumepy.utils"
