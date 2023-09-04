"""Module pytest for files module."""

import logging
import re
from pathlib import Path
from shutil import rmtree
from tempfile import gettempdir

import pytest

from incolumepy.utils.files import realfilename

__author__ = "@britodfbr"  # pragma: no cover
test_dir = Path(gettempdir()) / Path(__file__).stem
# rmtree(test_dir.as_posix(), ignore_errors=True)
# test_dir.mkdir(exist_ok=True, parents=True)


@pytest.mark.parametrize(
    ("entrance", "expected"),
    [
        ("version.txt", True),
        ("README.md", True),
    ],
)
def test_realfilename_not_null(entrance, expected, caplog):
    """Verify realfilename is not None."""
    assert realfilename(entrance) is not None


@pytest.mark.parametrize(
    ("entrance", "expected"),
    [
        ("version.txt", True),
        ("README.txt", True),
    ],
)
def test_realfilename_suggested_name(entrance, expected, caplog):
    """Verify realfilename suggested name on log."""
    caplog.set_level(logging.INFO)
    assert realfilename(entrance)
    assert caplog.messages == []

    with caplog.at_level(logging.ERROR):
        realfilename(entrance)
        assert caplog.messages == []

    with caplog.at_level(logging.DEBUG):
        realfilename(entrance)
        assert caplog.messages == [f"Suggested name: {entrance}"]
        assert re.compile(
            r"\d{4}(-\d{2}){2}T\d{2}(:\d{2}){2}; DEBUG\s+; root; files; "
            r"realfilename; Suggested name: .+\n",
            flags=re.I,
        ).fullmatch(caplog.text)


@pytest.mark.parametrize(
    ("entrance", "expected"),
    [
        # filebase sem extensão > .dat
        (
            {
                "filebase": (
                    test_dir / "britodfbr" / "diretorio" / "para" / "teste"
                ).as_posix(),
                "ext": ".dat",
                "separador": True,
            },
            (test_dir / "britodfbr" / "diretorio" / "para" / "teste")
            .with_suffix(".dat")
            .as_posix(),
        ),
        # filebase sem extensão > .md
        (
            {
                "filebase": (
                    test_dir / "diretorio" / "para" / "teste"
                ).as_posix(),
                "ext": ".md",
                "separador": True,
            },
            (test_dir / "diretorio" / "para" / "teste")
            .with_suffix(".md")
            .as_posix(),
        ),
        # filebase .json > .bash
        (
            {
                "filebase": (test_dir / "teste" / "test.json").as_posix(),
                "ext": ".bash",
                "separador": True,
            },
            (test_dir / "teste" / "test.json").with_suffix(".bash").as_posix(),
        ),
        # filebase sem extensão > .txt (default)
        (
            {
                "filebase": (test_dir / "teste" / "lll").as_posix(),
                "separador": True,
            },
            (test_dir / "teste" / "lll").with_suffix(".txt").as_posix(),
        ),
    ],
)
def test_realfilename_sugestion_name(entrance, expected):
    """Verify realfilename with parameters."""
    assert realfilename(**entrance).as_posix() == expected


@pytest.mark.parametrize(
    ("filebase", "entrance", "fileoutput"),
    [
        pytest.param(
            test_dir / "teste" / "report.json",
            {},
            "report_05.json",
            # marks=pytest.mark.skip(reason="Ops...")
        ),
        # filebase .json > .txt
        pytest.param(
            test_dir / "teste" / "lll.json",
            {
                "separador": False,
            },
            "lll05.json",
            # marks=pytest.mark.skip(reason="Ops...")
        ),
        # filebase .json > .txt
        pytest.param(
            test_dir / "teste" / "report.log",
            {
                "separador": True,
            },
            "report_05.log",
            # marks=pytest.mark.skip(reason="Ops...")
        ),
        pytest.param(
            test_dir / "registro.xml",
            {
                "separador": False,
                "digits": 3,
            },
            "registro005.xml",
        ),
    ],
)
def test_realfilename_with_exists_files(entrance, filebase, fileoutput):
    """Verify realfilename with parameters and exists files."""
    entrance["filebase"] = filebase.as_posix()

    rmtree(test_dir.as_posix(), ignore_errors=True)
    filebase.parent.mkdir(exist_ok=True, parents=True)
    file: Path = Path()
    for _ in range(6):
        file = Path(realfilename(**dict(entrance)))
        file.write_text(".")
    fileout = filebase.with_name(f"{fileoutput}").with_suffix(filebase.suffix)
    assert file.as_posix() == fileout.as_posix()


@pytest.mark.parametrize(
    ("filebase", "entrance", "expected"),
    [
        pytest.param(
            test_dir / "test" / "teste" / "testes" / "file.md",
            {"separador": False, "ext": "sh"},
            "file01.sh",
            # marks=pytest.mark.skip(reason="Only skip")
        ),
        pytest.param(
            test_dir / "test" / "file.md",
            {"separador": False, "ext": "xml"},
            "file01.xml",
            # marks=pytest.mark.skip(reason="Only skip")
        ),
        pytest.param(
            test_dir / "file.md",
            {"separador": False, "ext": "bash"},
            "file01.bash",
            # marks=pytest.mark.skip(reason="Only skip")
        ),
        pytest.param(
            test_dir / "file.md",
            {"separador": True, "ext": "dat"},
            "file_01.dat",
            # marks=pytest.mark.skip(reason="Only skip")
        ),
        pytest.param(
            test_dir / "file.md",
            {
                "separador": False,
                "digits": 4,
                "ext": "log",
            },
            "file0001.log",
            # marks=pytest.mark.skip(reason="Only skip")
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 5, "ext": "log", "separador": True},
            "filename_00001.log",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 5, "ext": "csv", "separador": True},
            "filename_00001.csv",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 3, "ext": "log", "separador": True},
            "filename_001.log",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 4, "ext": "log", "separador": True},
            "filename_0001.log",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 1, "ext": "log", "separador": True},
            "filename_1.log",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.log",
            {"ext": "md", "separador": True},
            "filename_01.md",
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
    ],
)
def test_realfilename_digits_output(filebase, entrance, expected):
    filebase.parent.mkdir(exist_ok=True, parents=True)
    filebase.with_suffix(f".{entrance['ext']}").write_text("")
    entrance["filebase"] = filebase.as_posix()
    file = Path(realfilename(**entrance))
    assert file.as_posix() == (filebase.parent / expected).as_posix()


@pytest.mark.parametrize(
    ("filebase", "entrance"),
    [
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 1, "ext": "log", "separador": False},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 1, "ext": "log", "separador": True},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"ext": "log", "separador": False},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"ext": "log", "separador": True},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 3, "ext": "log", "separador": False},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 3, "ext": "log", "separador": True},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 4, "ext": "log", "separador": False},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 4, "ext": "log", "separador": True},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 5, "ext": "log", "separador": False},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
        pytest.param(
            test_dir / "filename.txt",
            {"digits": 5, "ext": "log", "separador": True},
            # marks=pytest.mark.skip(reason="Not implemented yet."),
        ),
    ],
)
def test_realfilename_exists(filebase, entrance):
    entrance["filebase"] = filebase.as_posix()
    file = Path(realfilename(**entrance))
    file.write_text(" ")
    assert file.is_file() is True
    file.unlink()
