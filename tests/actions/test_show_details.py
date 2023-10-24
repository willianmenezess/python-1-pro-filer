from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import date


def test_show_details_exist_file(capsys):
    """Testa se show_details mostra os detalhes de um arquivo existente,
    o qual foi criado aqui no teste"""
    context = {"base_path": "test.txt"}
    # arquivo .txt criado, mas vazio
    with open(context["base_path"], "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File name: test.txt\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .txt\n"
        "Last modified date:"
        f" {date.fromtimestamp(os.path.getmtime(context['base_path']))}\n"
    )


def test_show_details_not_exist_file(capsys):
    """Testa se show_details mostra uma mensagem de erro para um arquivo
    inexistente"""
    context = {"base_path": "xablau.txt"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File 'xablau.txt' does not exist\n"
    )


def test_show_details_not_extension(capsys):
    """Testa se show_details mostra 'no extension' para um arquivo
    existente, mas sem ser informada a extensão"""
    context = {"base_path": "test"}
    # arquivo criado sem extensão
    with open(context["base_path"], "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "File name: test\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date:"
        f" {date.fromtimestamp(os.path.getmtime(context['base_path']))}\n"
    )
