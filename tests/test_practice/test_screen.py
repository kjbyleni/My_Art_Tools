import pygame
import pytest
from practice.screen import Screen, Time


@pytest.fixture
def screen_gen():
    pygame.init()
    return Screen(pygame.display)


def test_full_screen_active_size_full_screen_by_default(screen_gen):
    assert screen_gen.get_active_size() == screen_gen.full_screen


def test_toggle_full_screen(screen_gen):
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
    # event = pygame.event.post(event)
    screen_gen.toggle_full_screen(event)
    assert screen_gen.get_active_size() == screen_gen.default_size


def test_toggle_full_screen_then_back_to_full_screen(screen_gen):
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
    # event = pygame.event.post(event)
    screen_gen.toggle_full_screen(event)
    screen_gen.toggle_full_screen(event)
    assert screen_gen.get_active_size() == screen_gen.full_screen


@pytest.fixture
def time_gen():
    return Time(1)


def test_time_between_images(time_gen):
    one_minute = 60000
    assert time_gen.time_between_images == one_minute


def test_update_ticks(time_gen):
    time_gen.old_ticks = -1000
    assert time_gen.update_ticks() == time_gen.old_ticks
