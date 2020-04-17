import json
import os
from tkinter import filedialog

saved_storage = 'path.json'


def read_in_paths():
    is_file = os.path.isfile(saved_storage)
    with open(saved_storage, 'r' if is_file else 'w+') as paths:
        if is_file:
            file_data = json.load(paths)
        else:
            file_data = {}
            paths.write("{}")
            paths.close()
    return file_data


def get_path_with_key(key):
    file_data = read_in_paths()
    return file_data[key]


def remove_folder_path(key):
    file_data = read_in_paths()
    file_data.pop(key, None)
    temp_lst = json.dumps(file_data, indent=4)
    f = open(saved_storage, 'w+')
    f.write(temp_lst)
    f.close()


def get_path(path_index):
    with open('path.txt', "r") as paths_file:
        file_array = paths_file.readlines()
    return file_array[path_index].rstrip()


def print_items(items):
    for item in items:
        print(f'\t\t{item}')


def print_result(items, context):
    print(
        '\n\t',
        f'---------   Creating your {context}  ---------'
    )
    print_items(items)
    print(f'\t -----------   {context} Created!   -----------\n')


def validate_is_number(how_many=None, attempt=0, msg="How Many? "):
    if how_many is None:
        how_many = input(msg)
    try:
        return int(how_many)
    except ValueError:
        print("input must be a number")
        if attempt > 1:
            print("too many attempts!")
        else:
            validate_is_number(how_many=None, attempt=attempt + 1, msg=msg)


# edit_file requires a generator object
def edit_file(generator):
    tmp_path = './tmp_path.json'
    # print keys
    print_items(generator.get_keys())
    key = input("\nWhich list to modify? ")
    f = open(tmp_path, 'w')
    if key in generator.lst:
        for item in sorted(generator.lst[key]):
            # print existing list
            f.write(f'{item}\n')
        f.close()

        # open notepad.exe allow user to edit.  Wait until done editing
        os.system(f'notepad.exe {tmp_path}')
        generator.lst[key] = generator.convert_file_to_array(tmp_path)
        generator.export_lst()
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
            print("SUCCESS!")
