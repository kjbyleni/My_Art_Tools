from enum import Enum
from random import randint

import os
import pygame

import lib.utils as utils
from practice.pygame_utils import Screen


class PathOptions(Enum):
    FIGURE = 0
    LANDSCAPE = 1


class ImageManager:
    def __init__(self, images_path_index: int, screen: Screen):
        self.images = Images(images_path_index)
        self.screen = screen
        self.current_img = None
        self.images_displayed = []

    def scale_image(self, img: pygame.image):
        w, h = self.screen.get_active_size()
        width, height = img.get_rect().size
        scale_width = w / width
        scale_height = h / height
        if width > height:  # landscape
            height_with_scaled_width = int(height * scale_width)
            if height_with_scaled_width > h:
                size = int(width * scale_height), int(height * scale_height)
            else:
                size = int(width * scale_width), height_with_scaled_width
        else:
            size = int(width * scale_height), int(height * scale_height)
        return pygame.transform.scale(img, size)

    def get_previous_image(self):
        if len(self.images_displayed) > 1:
            return self.images_displayed[-2]
        else:
            return self.images_displayed[-1]

    def build_next_image(self):
        img_to_show = self.images.get_rand_image()
        print(img_to_show)
        fig_img = pygame.image.load(img_to_show)
        self.current_img = self.scale_image(fig_img)
        self.images_displayed.append(self.current_img)
        return self.current_img

    def get_coords_to_center_image(self, image_size):
        w, h = self.screen.get_active_size()
        width, height = image_size
        width_diff = w - width
        height_diff = h - height
        return int(width_diff / 2), int(height_diff / 2)

    def display_current_image(self):
        if self.current_img is None:
            self.build_next_image()
        centered_size = self.get_coords_to_center_image(self.current_img.get_rect().size)
        self.screen.display.blit(self.current_img, centered_size)


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
