import os
from pathlib import Path
from tempfile import gettempdir

msg = "fake content"
fout = Path(gettempdir(), "fake.file").resolve()

fout.write_text(msg)

print(f'message "{msg}", write with success into {fout}, {os.uname()} ')
