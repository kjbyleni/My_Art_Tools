import pygame

from practice.generate_pic import FigureDrawing
from practice.screen import Screen

MINUTES = 1000 * 60


class PictureViewer:

    def __init__(self, images_path, time_between_images=1):
        pygame.init()
        # setup stages
        self.stages = []
        self.images_shown_in_stage = 0
        self.total_images_to_show_for_stage = 10
        self.time_between_images = time_between_images * MINUTES

        #setup picture viewer
        self.screen = Screen(pygame.display)
        self.figures = FigureDrawing(images_path)
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.old_ticks = None
        self.current_img = None

    def display_image(self, image_to_display):
        w, h = self.screen.get_active_size()
        width, height = image_to_display.get_rect().size
        width_diff = w - width
        height_diff = h - height
        centered_size = int(width_diff / 2), int(height_diff / 2)
        self.screen.display.blit(image_to_display, centered_size)

    def scale_image(self, img: pygame.image):
        w, h = self.screen.get_active_size()
        width, height = img.get_rect().size
        scale_width = w / width
        scale_height = h / height
        if width > height:  # landscape
            size = int(width * scale_width), int(height * scale_width)
        else:
            size = int(width * scale_height), int(height * scale_height)
        return pygame.transform.scale(img, size)

    def build_image(self):
        img_to_show = self.figures.get_rand_image()
        print(img_to_show)
        fig_img = pygame.image.load(img_to_show)
        return self.scale_image(fig_img)

    def display_images(self):
        current_ticks = pygame.time.get_ticks()
        time_elapsed_between_image = current_ticks - self.old_ticks
        if time_elapsed_between_image >= self.time_between_images:
            self.current_img = self.build_image()
            self.old_ticks = pygame.time.get_ticks()
            self.images_shown_in_stage += 1
            self.next_stage()

        self.display_image(self.current_img)

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

    def show(self, stages=[]):
        self.current_img = self.build_image()
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
