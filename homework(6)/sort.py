import os
import shutil
from const import image, video, document, music, archives, folders_for_sort  # import our constants to avoid big code


# function for sorting folders
def sorting(name_folder, first_path):
    os.chdir(name_folder)
    file_unknown = []
    folders = []
    test = {
        image: 'images',
        video: 'video',
        document: 'documents',
        music: 'music',
    }

    # Viewing all files in a folder
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
                folders.append(normalize(name_folder=name_folder, file_name=i))

    print(f'File unknowns: {file_unknown} in path: {name_folder}')

    # Recursion for subfolders
    for i in folders:
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


def del_empty_dirs(path):
    for d in os.listdir(path):
        if d not in folders_for_sort:
            a = os.path.join(path, d)
            if os.path.isdir(a):
                del_empty_dirs(a)
                if not os.listdir(a):
                    os.rmdir(a)


if __name__ == '__main__':
    name_folder = input('Enter the path to the file\n')
    first_path = name_folder  # Keeping the original path
    del_empty_dirs(first_path)  # To optimize, first delete all empty folders
    sorting(name_folder, first_path)  # Sorting folders
    os.chdir(name_folder)  # Returning to the original folder
    del_empty_dirs(first_path)  # Delete new empty folders
