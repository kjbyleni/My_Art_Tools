import pygame

import lib.utils as utils
from practice.generate_pic import FigureDrawing
from practice.screen import Screen, Time


class ImageManager:
    def __init__(self, images_path, screen: Screen):
        self.images = FigureDrawing(images_path)
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


class ImageSequence:
    def __init__(self, time_between_images: int, total_images_to_show: int):
        self.time_between_images = time_between_images,
        self.total_images_to_show = total_images_to_show
        self.images_shown = 0

    def is_sequence_done(self):
        return self.images_shown >= self.total_images_to_show

    def image_to_display_for_sequence_time(self, time: Time, img_manager: ImageManager):
        time_elapsed_between_image = time.get_ticks() - time.old_ticks
        if time_elapsed_between_image >= time.time_between_images:
            img_manager.build_next_image()
            time.update_ticks()
            self.images_shown += 1

        img_manager.display_current_image()


class ImageSequenceList:
    def __init__(self, sequence_list, path_index, screen: Screen):
        self.img_path = utils.get_path(path_index=path_index)
        self.img_manager = ImageManager(self.img_path, screen)
        self.sequence_list = sequence_list
        self.sequence = None

    def is_end_of_sequence_list(self):
        return len(self.sequence_list) == 0

    def execute_sequence(self, time: Time):
        if not self.is_end_of_sequence_list():
            time_between, total_images = self.sequence_list[0]
            self.sequence = ImageSequence(time_between, total_images)
            self.sequence.image_to_display_for_sequence_time(time, self.img_manager)

    def execute_sequence_list(self, time: Time):
        if self.sequence is None:
            self.execute_sequence(time)
        else:
            if self.sequence.is_sequence_done():
                if self.is_end_of_sequence_list():
                    return True
                else:
                    self.sequence_list.pop(0)
                    self.execute_sequence(time)
            else:
                self.sequence.image_to_display_for_sequence_time(time, self.img_manager)
        return False

    def handle_events_for_sequence(self, event, time: Time):
        if event.type is pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.img_manager.build_next_image()
            time.update_ticks()
        elif event.type is pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.img_manager.current_img = self.img_manager.get_previous_image()
            time.update_ticks()
