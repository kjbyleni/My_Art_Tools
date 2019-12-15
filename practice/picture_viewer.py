import pygame

from practice.screen import Screen
from practice.image_manager import ImageManager

MINUTES = 1000 * 60


class PictureViewer:

    def __init__(self, images_path, time_between_images=1):
        pygame.init()
        # setup stages
        self.stages = []
        self.images_shown_in_stage = 0
        self.total_images_to_show_for_stage = 10
        self.time_between_images = time_between_images * MINUTES

        # setup picture viewer
        self.screen = Screen(pygame.display)
        self.img_manager = ImageManager(images_path, self.screen)
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.old_ticks = None

    def next_stage(self):
        if self.images_shown_in_stage >= self.total_images_to_show_for_stage:
            self.stages.pop(0)
            if len(self.stages) > 0:
                self.stage(self.stages[0])
            else:
                self.crashed = True

    def stage(self, stg_info=(1, 5)):
        time, how_many = stg_info
        self.time_between_images = time * MINUTES
        self.total_images_to_show_for_stage = how_many
        self.images_shown_in_stage = 0

    def display_images(self):
        current_ticks = pygame.time.get_ticks()
        time_elapsed_between_image = current_ticks - self.old_ticks
        if time_elapsed_between_image >= self.time_between_images:
            self.img_manager.build_image()
            self.old_ticks = pygame.time.get_ticks()
            self.images_shown_in_stage += 1
            self.next_stage()

        self.img_manager.display_image()

    def show(self, stages=[]):
        self.img_manager.build_image()
        self.old_ticks = pygame.time.get_ticks()
        self.stages = stages

        if len(self.stages) > 0:
            self.stage(self.stages[0])

        while not self.crashed:
            self.display_images()
            pygame.display.update()
            self.clock.tick(20)

            for event in pygame.event.get():
                self.screen.toggle_full_screen(event)
                if event.type == pygame.QUIT:
                    self.crashed = True

        pygame.quit()
        quit()
