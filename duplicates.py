import os


def crawl(path):
    files_dict = {}
    for (dir_path, dir_names, file_names) in os.walk(path):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            if files_dict.get(file) is None:
                files_dict[file] = {'size': os.path.getsize(file_path),
                                    'path': file_path}
            elif os.path.getsize(file_path) == files_dict[file]['size']:
                print('Найдено совпадение!\n'
                      '{0}\n'
                      '{1}\n'
                      'Размер: {2}'.format(file_path,
                                           files_dict[file]['path'],
                                           files_dict[file]['size']))


if __name__ == '__main__':
    crawl(input('Введите путь к папке: '))
