from pro_filer.actions.main_actions import show_preview  # NOQA
# from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "mock_context, expected",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            (
                "Found 3 files and 2 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', "
                "'src/utils/__init__.py']\n"
                "First 5 directories: ['src', 'src/utils']\n"
            ),
        ),
        (
            {"all_files": [], "all_dirs": []},
            (
                "Found 0 files and 0 directories\n"
            ),
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": [],
            },
            (
                "Found 3 files and 0 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', "
                "'src/utils/__init__.py']\n"
                "First 5 directories: []\n"
            ),
        ),
        (
            {
                "all_files": [],
                "all_dirs": ["src", "src/utils"],
            },
            (
                "Found 0 files and 2 directories\n"
                "First 5 files: []\n"
                "First 5 directories: ['src', 'src/utils']\n"
            ),
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                    "src/utils/aux.py",
                    "src/utils/aux2.py",
                    "src/utils/aux3.py",
                ],
                "all_dirs": [
                    "src",
                    "src/utils"
                ],
            },
            (
                "Found 6 files and 2 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', "
                "'src/utils/__init__.py', 'src/utils/aux.py', "
                "'src/utils/aux2.py']\n"
                "First 5 directories: ['src', 'src/utils']\n"
            ),
        ),
    ],
)
def test_show_preview_sucess(capsys, mock_context, expected):
    show_preview(mock_context)
    captured = capsys.readouterr()
    assert captured.out == expected
