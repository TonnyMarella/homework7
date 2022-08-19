import os
import shutil
import re
import sys
from pathlib import Path

from clean_folder.const import *  # import our constants to avoid big code


def sorting(folder_name: str, first_path: str):
    """
    Viewing all files in a folder
    :param folder_name:
    :param first_path:
    :return:
    """
    os.chdir(folder_name)
    file_unknown = []
    folders = []
    test = {
        image: 'images',
        video: 'video',
        document: 'documents',
        music: 'music',
    }

    for i in os.listdir(folder_name):
        if os.path.isfile(i):
            file = normalize(folder_name=folder_name, file_name=i)
            format_file = file.split('.')[1].upper()
            count = 0
            try:
                if format_file in archives:
                    shutil.unpack_archive(os.path.join(os.getcwd(), i), os.path.join(first_path, 'archives', i[:-3]))
            except shutil.ReadError as error:
                print(error)
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
                folders.append(normalize(folder_name=folder_name, file_name=i))

    print(f'File unknowns: {file_unknown} in path: {folder_name}')
    recursion_subfolders(folders=folders, folder_name=folder_name, first_path=first_path)


def recursion_subfolders(folders: list, folder_name: str, first_path: str):
    """
    Recursion for subfolders
    :param folders:
    :param folder_name:
    :param first_path:
    """
    for i in folders:
        sorting(folder_name=os.path.join(folder_name, i), first_path=first_path)


def normalize(folder_name: str, file_name: str) -> str:
    """
    Translates a word
    :param folder_name:
    :param file_name:
    :return: translated word
    """
    new_file_name = re.sub(r'[^.\w]', '_', file_name)
    result = ''

    for i in new_file_name:
        if i in translate:
            i = translate[i]
        result += i

    os.renames(os.path.join(folder_name, file_name), os.path.join(folder_name, result))
    return result


def del_empty_dirs(path: str) -> bool:
    if os.path.exists(path) and Path(path).is_dir():
        for d in os.listdir(path):
            if d not in folders_for_sort:
                a = os.path.join(path, d)
                if os.path.isdir(a):
                    del_empty_dirs(a)
                    if not os.listdir(a):
                        os.rmdir(a)
        return True
    else:
        return False


def main():
    folder_name = sys.argv[1]
    first_path = folder_name  # Keeping the original path
    if del_empty_dirs(first_path):  # To optimize, first delete all empty folders
        sorting(folder_name, first_path)  # Sorting folders
        os.chdir(folder_name)  # Returning to the original folder
        del_empty_dirs(first_path)  # Delete new empty folders
    else:
        raise Exception('Enter the correct path')
