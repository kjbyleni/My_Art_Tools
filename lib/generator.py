import json
import os

from random import randint
from ideas.user_messenger import Messenger


class Generator:

    def __init__(self, context='general', gen_path='./ideas/ideas.txt', mod_path='./ideas/tmp.txt'):
        self.mod_path = mod_path
        self.gen_path = gen_path
        self.context = context
        self.message = Messenger
        self.rand_items = []
        with open(self.gen_path, 'r') as json_file:
            self.lst = json.load(json_file)

    def get_keys(self):
        return list(self.lst.keys())

    # Method has no unit tests
    def edit_lst(self, key):
        f = open(self.mod_path, 'w')
        if key in self.lst:
            for item in sorted(self.lst[key]):
                f.write(f'{item}\n')
            f.close()
            os.system(f'notepad.exe {self.mod_path}')
            self.lst[key] = Generator.convert_file_to_array(self.mod_path)
            self.export_lst()
            if os.path.exists(self.mod_path):
                os.remove(self.mod_path)
                Messenger.success()

    def export_lst(self, export_to=None):
        if export_to is None:
            export_to_path = self.gen_path
        else:
            export_to_path = export_to
        temp_lst = json.dumps(self.lst, indent=4)
        f = open(export_to_path, 'w+')
        f.write(temp_lst)
        f.close()

    def get_rand_item(self, key):
        rand_num = randint(0, (len(self.lst[key]) - 1))
        if self.lst[key][rand_num] in self.rand_items:
            rand_num = randint(0, (len(self.lst[key]) - 1))
        self.rand_items.append(self.lst[key][rand_num])

    def generate(self):
        for key in self.lst:
            self.get_rand_item(key)
        self.print_result()

    def print_result(self):
        Messenger.print_result(self.rand_items, self.context)

    @staticmethod
    def convert_file_to_array(file_location):
        with open(file_location, "r") as file_to_convert:
            file_array = file_to_convert.readlines()

        stripped_array = []
        for item in file_array:
            stripped_array.append(item.strip())
        return stripped_array
