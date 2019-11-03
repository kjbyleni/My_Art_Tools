import json
import os

from random import randint
from ideas.user_messenger import Messenger


class Generator:
    GENERATOR_PATH = './ideas/ideas.txt'
    MODIFY_PATH = './ideas/tmp.txt'

    def __init__(self, context='general'):
        self.context = context
        self.keys = []
        self.message = Messenger
        self.rand_items = []
        with open(Generator.GENERATOR_PATH, 'r') as json_file:
            self.lst = json.load(json_file)

    def get_keys(self):
        return list(self.lst.keys())

    def edit_lst(self, key):
        f = open(Generator.MODIFY_PATH, 'w')
        if key in self.lst:
            for item in sorted(self.lst[key]):
                f.write(f'{item}\n')
            f.close()
            os.system(f'notepad.exe {Generator.MODIFY_PATH}')
            self.lst[key] = Generator.convert_file_to_array(Generator.MODIFY_PATH)
            self.export_lst()
            if os.path.exists(Generator.MODIFY_PATH):
                os.remove(Generator.MODIFY_PATH)
                Messenger.success()

    def export_lst(self):
        temp_lst = json.dumps(self.lst, indent=4)
        f = open(Generator.GENERATOR_PATH, 'w')
        f.write(temp_lst)
        f.close()

    def get_rand_item(self, key):
        rand_num = randint(0, (len(self.lst[key]) - 1))
        if self.lst[key][rand_num] in self.rand_items:
            rand_num = randint(0, (len(self.lst[key]) - 1))
        self.rand_items.append(self.lst[key][rand_num])

    def generate(self):
        for key in self.keys:
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
