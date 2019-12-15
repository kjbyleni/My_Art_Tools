from builtins import len
from os import walk, path
from random import randint


class FigureDrawing:

    def __init__(self, path_to_pics: str):
        self.path_to_pics = path_to_pics
        self.img_exts = ["jpg", "jpeg", "png"]
        self.exclude = ["PoseOverview"]
        self.files_in_path = self.get_files_in_folder(exclude=self.exclude,
                                                      with_extensions=self.img_exts)

    def get_rand_image(self):
        rand_num = randint(0, (len(self.files_in_path) - 1))
        return self.files_in_path[rand_num]

    def get_rand_images(self, how_many: int):
        items = []
        for i in range(0, how_many):
            items.append(self.get_rand_image())
        return items

    # def generate_pic(self, how_many: int):
    #     min_value = 0
    #     max_value = 10
    #     if self.files_in_path is None:
    #         self.get_files_in_folder()
    #
    #     total = int(how_many)
    #     if min_value < total < max_value:
    #         for i in range(total):
    #             img = self.get_rand_image()
    #             webbrowser.open(img)
    #     else:
    #         print(f"must be {min_value} < how_many < {max_value}")

    def get_files_in_folder(self, exclude=['PoseOverview'], with_extensions=['jpg']):
        files_in_path = []
        for r, d, f in walk(self.path_to_pics):
            for file in f:
                joined_file = path.join(r, file)
                if any(ext in joined_file for ext in with_extensions):
                    if not any(exc in exclude for exc in joined_file):
                        files_in_path.append(joined_file)

        return files_in_path
