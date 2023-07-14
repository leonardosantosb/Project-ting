from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_names = [data['nome_do_arquivo'] for data in instance.queue]
    if path_file in file_names:
        print(f'O arquivo {path_file} já foi processado anteriormente.')
        return

    lines = txt_importer(path_file)
    if lines:
        file_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(lines),
            'linhas_do_arquivo': lines
        }
        instance.enqueue(file_data)
        print(file_data)
    else:
        print(f'Não foi possível processar o arquivo {path_file}.')


def remove(instance):
    try:
        file_data = instance.dequeue()
        file_path = file_data["nome_do_arquivo"]
        print(f"Arquivo {file_path} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
