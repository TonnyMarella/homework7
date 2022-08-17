import os
import shutil
from const import image, video, document, music, archives


def sorting(name_folder, first_path):
    os.chdir(name_folder)

    folders_for_sort = ['archives', 'audio', 'documents', 'images', 'video']
    test = {
        image: 'images',
        video: 'video',
        document: 'documents',
        music: 'music',
    }
    file_unknown = []
    folders = []
    for i in os.listdir(name_folder):
        if os.path.isfile(i):
            file = normalize(name_folder=name_folder, file_name=i)
            format_file = file.split('.')[1].upper()
            count = 0
            if format_file in archives:
                shutil.unpack_archive(os.path.join(os.getcwd(), i), os.path.join(first_path, 'archives', i[:-3]))
            else:
                for keys, values in test.items():
                    if format_file in keys:
                        os.replace(os.path.join(os.getcwd(), file), os.path.join(first_path, values, file))
                        count += 1
                        break
                if count == 0:
                    file_unknown.append(i)

        elif os.path.isdir(i):
            if i not in folders_for_sort:
                a = os.path.join(name_folder, i)
                if not os.listdir(a):
                    os.rmdir(a)
                else:
                    folders.append(normalize(name_folder=name_folder, file_name=i))
    print('folders', folders)

    print(f'File unknowns: {file_unknown} in path: {name_folder}')

    for i in folders:
        print('in', os.path.join(name_folder, i))
        sorting(name_folder=os.path.join(name_folder, i), first_path=first_path)


def normalize(name_folder, file_name):
    import re
    from const import translate

    new_file_name = re.sub(r'[^.\w]', '_', file_name)
    result = ''

    for i in new_file_name:
        if i in translate:
            i = translate[i]
        result += i

    os.renames(os.path.join(name_folder, file_name), os.path.join(name_folder, result))
    return result


if __name__ == '__main__':
    name_folder = input('Enter the path to the file\n')
    first_path = name_folder
    sorting(name_folder, first_path)
