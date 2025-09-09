"""incolumepy.utils module."""

from contextlib import suppress
from pathlib import Path

with suppress(ImportError, ModuleNotFoundError):
    import tomllib as tomli  # type: ignore[import]

with suppress(ImportError, ModuleNotFoundError):
    import tomli  # type: ignore[import]

confproject = Path(__file__).parents[3] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'

with suppress(FileNotFoundError), confproject.open('rb') as f:
    versionfile.write_text(tomli.load(f)['project']['version'] + '\n')

__version__ = versionfile.read_text().strip()
__title__ = 'incolume.py.utils'
