import pygame

from practice.pygame_utils import Screen, Time
from practice.sequence_handler import ImageSequenceList


class PictureViewer:

    def __init__(self, time_between_images=1):
        pygame.init()
        # setup stages
        self.stages = []
        self.images_shown_in_stage = 0
        self.total_images_to_show_for_stage = 10

        # setup picture viewer
        self.screen = Screen(pygame.display)
        self.time = Time(time_between_images)
        self.crashed = False

    def show(self, img_path_index, sequence_list=[]):
        sequences = ImageSequenceList(sequence_list, img_path_index, self.screen)

        while not self.crashed:
            self.screen.display.fill((0, 0, 0))
            self.crashed = sequences.execute_sequence_list(self.time)
            pygame.display.update()

            for event in pygame.event.get():
                self.screen.toggle_full_screen(event)
                sequences.handle_events_for_sequence(event, self.time)
                if event.type == pygame.QUIT:
                    self.crashed = True

        pygame.quit()
        quit()
