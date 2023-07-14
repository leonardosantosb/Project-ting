def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        lines = file_data["linhas_do_arquivo"]
        occurrences = []

        for j, line in enumerate(lines):
            if word.lower() in line.lower():
                occurrence = {"linha": j + 1}
                occurrences.append(occurrence)

        if occurrences:
            file_result = {
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences
            }
            result.append(file_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
