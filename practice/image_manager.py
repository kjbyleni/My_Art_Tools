import os
from random import randint

import lib.utils as utils


class Images:

    def __init__(self, image_path_index: int):
        self.path_to_pics = utils.get_path(path_index=image_path_index)
        self.img_exts = ["jpg", "jpeg", "png"]
        self.exclude = ["PoseOverview"]
        self.files_in_path = self.get_files_in_folder(exclude=self.exclude,
                                                      with_extensions=self.img_exts)

    def get_rand_image(self):
        files_len = len(self.files_in_path)
        if files_len > 1:
            rand_num = randint(0, (len(self.files_in_path) - 1))
        elif files_len == 1:
            rand_num = 0
        else:
            raise Exception("No files were found! Look at path and try again.")
        return self.files_in_path[rand_num]

    def get_files_in_folder(self, exclude=['PoseOverview'], with_extensions=['jpg']):
        files_in_path = []
        if os.path.isfile(self.path_to_pics):
            files_in_path.append(self.path_to_pics)
        elif os.path.isdir(self.path_to_pics):
            for r, d, f in os.walk(self.path_to_pics):
                for file in f:
                    joined_file = os.path.join(r, file)
                    if any(ext in joined_file for ext in with_extensions):
                        if not any(substring in joined_file for substring in exclude):
                            files_in_path.append(joined_file)
        else:
            raise Exception("No path was found!  Cannot locate files in folder.")

        return files_in_path
