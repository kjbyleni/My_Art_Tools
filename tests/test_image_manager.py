import pygame
import pytest
import os

from practice.image_manager import Images, ImageManager
from practice.pygame_utils import Screen


@pytest.fixture
def figure_image_gen():
    yield Images(0)


def test_files_in_path_has_no_duplicates(figure_image_gen):
    assert len(figure_image_gen.files_in_path) == len(set(figure_image_gen.files_in_path))


def test_files_in_path_is_not_empty(figure_image_gen):
    assert len(figure_image_gen.files_in_path) > 0


def test_files_excluded(figure_image_gen):
    for file in figure_image_gen.files_in_path:
        assert file.find('PoseOverview') == -1


def test_invalid_file_input():
    invalid_file_path_index = 3
    pygame.init()
    with pytest.raises(Exception):
        assert Images(invalid_file_path_index, Screen(pygame.display, full_screen_mode=False))


def test_invalid_folder_input():
    invalid_folder_path_index = 4
    pygame.init()
    with pytest.raises(Exception):
        assert Images(invalid_folder_path_index, Screen(pygame.display, full_screen_mode=False))


@pytest.fixture
def image_man_gen():
    single_file_path_index = 2
    pygame.init()
    yield ImageManager(single_file_path_index, Screen(pygame.display, full_screen_mode=False))


def test_display_current_image_sets_image_if_new_instance(image_man_gen):
    assert image_man_gen.current_img is None
    image_man_gen.display_current_image()
    assert image_man_gen.current_img is not None


def test_tall_image_scales_correctly():
    tall_image_path_index = 5
    pygame.init()
    img = ImageManager(tall_image_path_index, Screen(pygame.display, full_screen_mode=False))
    img.display_current_image()
    assert img.current_img.get_rect().size == (628, 1000)


def test_wide_image_scales_correctly(image_man_gen):
    wide_image_path_index = 6
    pygame.init()
    img = ImageManager(wide_image_path_index, Screen(pygame.display, full_screen_mode=False))
    img.display_current_image()
    assert img.current_img.get_rect().size == (1500, 789)

