import os
from random import randint

import ideas.utils as utils


class Images:

    def __init__(self, path_key: int):
        self.path_to_pics = utils.get_path_with_key(key=path_key)
        self.img_exts = ["jpg", "jpeg", "png"]
        self.exclude = ["PoseOverview"]
        self.images_shown = PreviousArray()
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
        self.images_shown.append(self.files_in_path[rand_num])
        return self.images_shown.get_first()

    def get_previous_image(self):
        return self.images_shown.get_previous()

    def get_next_image(self):
        return self.images_shown.get_next()

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


class PreviousArray:
    def __init__(self):
        self.prev_index = None
        self.items = []

    def append(self, item):
        self.items.append(item)

    def get_next(self):
        if self.prev_index is None:
            if len(self.items) <= 0:
                return None
            else:
                if len(self.items) == 1:
                    return self.items[0]
                else:
                    return self.items[-1]
        else:
            if self.prev_index < 0:
                self.prev_index = 0

            self.prev_index += 1
            if (len(self.items) - 1) >= self.prev_index:
                return self.items[self.prev_index]
            else:
                return self.items[-1]

    def get_previous(self):
        if len(self.items) <= 0:
            return None
        elif len(self.items) == 1:
            return self.items[0]
        else:
            if self.prev_index is None:
                self.prev_index = len(self.items) - 2
                return self.items[self.prev_index]
            else:
                if self.prev_index >= len(self.items):
                    self.prev_index = len(self.items) - 1

                self.prev_index -= 1
                if self.prev_index >= 0:
                    return self.items[self.prev_index]
                else:
                    return self.items[0]

    def get_first(self):
        self.prev_index = None
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
