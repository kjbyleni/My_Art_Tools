import pygame


class Screen:

    def __init__(self, display: pygame.display):
        self.default_size = (1080, 900)
        self.offset = 40
        self.full_screen = (display.Info().current_w, display.Info().current_h)
        self.display = display.set_mode(self.full_screen, pygame.FULLSCREEN)
        pygame.display.set_caption("Image practice")

    def get_active_size(self):
        if self.display.get_flags() & pygame.FULLSCREEN:
            # full screen mode return full screen
            return self.full_screen
        else:
            return self.default_size

    def toggle_full_screen(self, event):
        if event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if self.display.get_flags() & pygame.FULLSCREEN:
                self.display = pygame.display.set_mode(self.default_size)
            else:
                self.display = pygame.display.set_mode(self.full_screen, pygame.FULLSCREEN)

    # def run_per_tick(self):
    #     self.display.fill((0, 0, 0))
