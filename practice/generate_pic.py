from builtins import len
from os import walk, path
from random import randint
import webbrowser


class FigureDrawing:

    def __init__(self, path_to_pics: str):
        self.files_in_path = None
        self.supported_img_extensions = ["jpg", "jpeg", "png"]
        self.exclude_files_that_contain = ["PoseOverview"]
        self.path_to_pics = path_to_pics
        pass

    def generate_pic(self, how_many: int):
        min_value = 0
        max_value = 10
        if self.files_in_path is None:
            self.get_images_in_folder(self.path_to_pics)

        total = int(how_many)
        if min_value < total < max_value:
            for i in range(total):
                rand_num = randint(0, (len(self.files_in_path) - 1))
                webbrowser.open(self.files_in_path[rand_num])
        else:
            print(f"must be {min_value} < how_many < {max_value}")

    def get_images_in_folder(self, folder_path: str):
        self.files_in_path = []
        for r, d, f in walk(folder_path):
            for file in f:
                joined_file = path.join(r, file)
                if any(ext in joined_file for ext in self.supported_img_extensions):
                    if not any(exclude in self.exclude_files_that_contain for exclude in joined_file):
                        self.files_in_path.append(joined_file)

        return self.files_in_path

