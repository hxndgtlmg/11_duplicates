import os


def crawl(path):
    files_dict = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
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
