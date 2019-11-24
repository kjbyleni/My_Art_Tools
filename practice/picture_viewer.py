import pygame

from practice.generate_pic import FigureDrawing

WIDTH = 1080
HEIGHT = 900
OFFSET = 40


class PictureViewer:
    _instance = None

    @staticmethod
    def get_instance(images_path):
        print("get_instance", PictureViewer._instance)
        if PictureViewer._instance is None:
            PictureViewer(images_path)
            return PictureViewer._instance
        else:
            return PictureViewer._instance

    def __init__(self, images_path):
        if PictureViewer._instance is not None:
            raise Exception("Game Is a singleton please call through Game.get_instance()")
        else:
            self.figures = FigureDrawing(images_path)

            pygame.init()
            self.display = pygame.display
            self.display.set_caption("Figure practice")
            self.game_display = self.display.set_mode((WIDTH + OFFSET, HEIGHT + OFFSET))
            self.clock = pygame.time.Clock()
            self.crashed = False

            # Return singleton object
            PictureViewer._instance = self

    def display_image(self, image_to_display):
        width, height = image_to_display.get_rect().size
        width_diff = (WIDTH + OFFSET) - width
        height_diff = (HEIGHT + OFFSET) - height
        centered_size = int(width_diff/2), int(height_diff/2)
        self.game_display.blit(image_to_display, centered_size)

    @staticmethod
    def scale_image(img: pygame.image, ideal_width=WIDTH, ideal_height=HEIGHT):
        width, height = img.get_rect().size
        scale_width = ideal_width / width
        scale_height = ideal_height / height
        if width > height:  # landscape
            size = int(width * scale_width), int(height * scale_width)
        else:
            size = int(width * scale_height), int(height * scale_height)
        return pygame.transform.scale(img, size)

    def show(self):
        img_to_show = self.figures.get_rand_image()
        fig_img = pygame.image.load(img_to_show)
        fig_img = self.scale_image(fig_img)

        while not self.crashed:
            self.game_display.fill((0, 0, 0))
            self.display_image(fig_img)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

            self.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()
