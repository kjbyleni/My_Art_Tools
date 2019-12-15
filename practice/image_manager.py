import pygame
from practice.generate_pic import FigureDrawing
from practice.screen import Screen


class ImageManager:
    def __init__(self, images_path, screen: Screen):
        self.images = FigureDrawing(images_path)
        self.screen = screen
        self.current_img = None

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
        img_to_show = self.images.get_rand_image()
        print(img_to_show)
        fig_img = pygame.image.load(img_to_show)
        self.current_img = self.scale_image(fig_img)
        return self.current_img

    def get_coords_to_center_image(self, image_size):
        w, h = self.screen.get_active_size()
        width, height = image_size
        width_diff = w - width
        height_diff = h - height
        return int(width_diff / 2), int(height_diff / 2)

    def display_image(self):
        centered_size = self.get_coords_to_center_image(self.current_img.get_rect().size)
        self.screen.display.blit(self.current_img, centered_size)

