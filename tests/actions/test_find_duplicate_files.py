from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


@pytest.mark.parametrize(
    "mock_context, expected",
    [
        (
            {
                "all_files": [
                    "./tests/__init__.py",
                    "./tests/actions/__init__.py",
                    "./pro_filer/__init__.py",
                ],
            },
            [
                ("./tests/__init__.py", "./tests/actions/__init__.py"),
                ("./tests/__init__.py", "./pro_filer/__init__.py"),
                ("./tests/actions/__init__.py", "./pro_filer/__init__.py"),
            ],
        ),
        (
            {
                "all_files": [
                    ".gitignore",
                    ".gitignore",
                ],
            },
            [(".gitignore", ".gitignore")],
        ),
        (
            {
                "all_files": [
                    "pro_filer/cli.py",
                    "pro_filer/cli_helpers.py"
                ]
            },
            []
        )
    ],
)
def test_find_duplicate_files(mock_context, expected):
    """Testa se a função find_duplicate_files retorna os pares de arquivos
    existentes que possuem o mesmo conteúdo, em forma de tuplas"""
    assert find_duplicate_files(mock_context) == expected


def test_find_duplicate_files_value_error():
    """Testa se a função find_duplicate_files retorna os pares de arquivos
    existentes que possuem o mesmo conteúdo, em forma de tuplas"""
    context = {
        "all_files": [
            ".gitignore",
            "src/app.py",
            "src/utils/__init__.py",
        ]
    }
    with pytest.raises(ValueError):
        find_duplicate_files(context)
