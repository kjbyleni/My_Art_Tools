from builtins import len
from os import walk, path
from random import randint

from PIL import Image

from practice.user_messenger import UserMessenger


class FigureDrawing:

    def __init__(self, path_to_pics):
        self.msg = UserMessenger()
        self.files_in_path = None
        self.supported_img_extensions = ["jpg", "jpeg", "png"]
        self.exclude_files_that_contain = ["PoseOverview"]
        self.path_to_pics = path_to_pics
        pass

    def generate_pic(self, how_many=None, attempt=0):
        min_value = 0
        max_value = 10
        if self.files_in_path is None:
            self.get_images_in_folder(self.path_to_pics)

        if how_many is None:
            how_many = self.msg.how_many()
        try:
            total = int(how_many)
            if 0 < total < 10:
                for i in range(total):
                    rand_num = randint(0, (len(self.files_in_path) - 1))
                    img = Image.open(self.files_in_path.__getitem__(rand_num))
                    img.show()
                    self.msg.success()
            else:
                self.msg.out_of_bounds(min_value, max_value)
        except ValueError:
            self.msg.input_must_be_number()
            if attempt > 1:
                self.msg.too_many_attempts()
            else:
                FigureDrawing.generate_pic(self, how_many=None, attempt=attempt + 1)

    def get_images_in_folder(self, folder_path):
        self.files_in_path = []
        for r, d, f in walk(folder_path):
            for file in f:
                joined_file = path.join(r, file)
                if any(ext in joined_file for ext in self.supported_img_extensions):
                    if not any(exclude in self.exclude_files_that_contain for exclude in joined_file):
                        self.files_in_path.append(joined_file)

        return self.files_in_path

    # def should_add_file(file_path, include_files_that_contain=[], exclude_files_that_contain=[]):
    #     for exclude in exclude_files_that_contain:
    #         if exclude in file_path:
    #             return False
    #
    #     # Any matching extensions should be included
    #     if not any(ext in file_path for ext in include_files_that_contain):
    #         # print("don't add file\n", file_path)
    #         return False
    #     return True
    # @staticmethod
    # def path_to_folder(key):
    #     path_helper = './lib/paths.txt'
    #     lst = {}
    #     if os._exists(path_helper):
    #         with open(path_helper, 'r') as json_file:
    #             lst = json.load(json_file)
    #     else:
    #         img_folder_path = input('Folder path to images? start from C:/')
    #         temp_lst = json.dumps({'images': img_folder_path}, indent=4)
    #         f = open(path_helper, 'w')
    #         f.write(temp_lst)
    #         f.close()
    #         FileHandler.path_to_folder()
