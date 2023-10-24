from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch


def test_show_disk_usage(capsys, tmp_path):
    """Testa se show_disk_usage mostra o uso de disco de um diretório
    existente, o qual foi criado aqui no teste"""
    # 2 arquivos .txt temporários criados com o mesmo conteúdo
    arch1 = tmp_path / "arquivo1.txt"
    arch2 = tmp_path / "arquivo2.txt"
    arch1.write_text("Palmeiras: Maior campeão")
    arch2.write_text("Palmeiras: Maior campeão do Brasil")
    context = {"all_files": [f"{arch1}", f"{arch2}"]}
    with patch("pro_filer.actions.main_actions._get_printable_file_path") as p:
        p.return_value = (
            "/tmp/pytest-of-pc/pytest-48..._show_disk_usage0"
        )
        show_disk_usage(context)
        captured = capsys.readouterr()
        assert captured.out == (
            "'/tmp/pytest-of-pc/pytest-48..._show_disk_usage0':"
            "                     35 (58%)\n"
            "'/tmp/pytest-of-pc/pytest-48..._show_disk_usage0':"
            "                     25 (41%)\n"
            "Total size: 60\n"
        )
    # a ordenação deve ser feita pelo tamanho do arquivo, do maior para o menor
        captured = capsys.readouterr()
        assert captured.out != (
            "'/tmp/pytest-of-pc/pytest-48..._show_disk_usage0':"
            "                     25 (41%)\n"
            "'/tmp/pytest-of-pc/pytest-48..._show_disk_usage0':"
            "                     35 (58%)\n"
            "Total size: 60\n"
        )


def test_show_disk_usage_with_empty_dir(capsys):
    """Testa se show_disk_usage mostra o uso de disco de um diretório
    vazio"""
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "Total size: 0\n"
    )


def test_show_disk_usage_long_length_file(capsys, tmp_path):
    file_long_path = (
        tmp_path / "quandosurgeoalviverdeimponentenogramadoemquealuta"
        "oaguardaavantipalestra.txt"
    )
    file_long_path.write_text("Palmeiras: Maior campeão do Brasil")
    context = {"all_files": [f"{file_long_path}"]}
    with patch("pro_filer.actions.main_actions._get_printable_file_path") as p:
        p.return_value = (
            "/tmp/pytest-of-pc/pytest-49..._show_disk_usage0"
        )
        show_disk_usage(context)
        captured = capsys.readouterr()
        assert captured.out == (
            "'/tmp/pytest-of-pc/pytest-49..._show_disk_usage0':"
            "                     35 (100%)\n"
            "Total size: 35\n"
        )
