import pygame

from practice.image_manager import ImageManager, PathOptions
from practice.pygame_utils import Screen, Time


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
    def __init__(self, sequence_list, image_path_index, screen: Screen):
        self.img_manager = ImageManager(image_path_index, screen)
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
                self.sequence_list.pop(0)
                if self.is_end_of_sequence_list():
                    return True
                else:
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
