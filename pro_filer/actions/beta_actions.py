"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    all_files = context["all_files"]
    if not all_files:
        print("No files found")
    else:
        deepest_file = max(all_files, key=lambda file: file.count("/"))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    all_files = context["all_files"]
    if not search_term:
        return []

    found_files = []

    for path in all_files:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name_lower = file_name.lower()
            search_term_lower = search_term.lower()

        if search_term in file_name or (
            not case_sensitive and search_term_lower in file_name_lower
        ):
            found_files.append(path)

    return found_files


# commit inicial


if __name__ == "__main__":
    context = {
        "all_files": [
            "/home/trybe/Downloads/Trybe_logo.png",
            "/home/trybe/Documents/aula/python/tests.py",
        ]
    }

    find_file_by_name(context, ".py")
    # Retorno: ["/home/trybe/Documents/aula/python/tests.py"]

    # find_file_by_name(context, "trybe", case_sensitive=False)
    # # Retorno: ["/home/trybe/Downloads/Trybe_logo.png"]

    # context = {"all_files": []}

    # find_file_by_name(context, "trybe")
    # # Retorno: []
