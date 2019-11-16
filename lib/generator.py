import json

from random import randint


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


class Generator:

    def __init__(self, context='general', keys=[], idea_path='./ideas/ideas.txt', temp_path='./ideas/tmp.txt'):
        self.temp_path = temp_path
        self.idea_path = idea_path
        self.context = context
        self.rand_items = []

        with open(self.idea_path, 'r') as json_file:
            self.lst = json.load(json_file)

        if len(keys) == 0:
            self.keys = self.lst.keys()
        else:
            self.keys = []

    def get_keys(self):
        return list(self.keys)

    def export_lst(self, export_to=None):
        if export_to is None:
            export_to_path = self.idea_path
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
        for key in self.keys:
            self.get_rand_item(key)
        self.print_result()

    def generate_multiple(self, how_many=None, key='items'):
        for i in range(how_many):
            self.get_rand_item(key)

    def print_result(self):
        print_result(self.rand_items, self.context)

    @staticmethod
    def convert_file_to_array(file_location):
        with open(file_location, "r") as file_to_convert:
            file_array = file_to_convert.readlines()

        stripped_array = []
        for item in file_array:
            stripped_array.append(item.strip())
        return stripped_array
