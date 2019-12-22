import pygame
import pytest

from practice.pygame_utils import Time, Screen
from practice.sequence_handler import ImageSequence, ImageSequenceList


@pytest.fixture
def img_sqnc():
    yield ImageSequence(1, 1)


def test_is_sequence_done_expect_false(img_sqnc):
    assert img_sqnc.is_sequence_done() == False


def test_is_sequence_done_expect_true(img_sqnc):
    img_sqnc.images_shown = 1
    assert img_sqnc.is_sequence_done() == True


@pytest.fixture
def img_sqnc_lst():
    pygame.init()
    screen = Screen(pygame.display, full_screen_mode=False)
    yield ImageSequenceList([(1, 2), (2, 4)], 0, screen)


def test_sequence_list_is_not_none(img_sqnc_lst):
    time = Time(1)
    assert img_sqnc_lst.sequence is None
    img_sqnc_lst.execute_sequence_list(time)
    assert img_sqnc_lst.sequence is not None


def test_sequence_list_sequence_is_done(img_sqnc_lst):
    time = Time(1)
    img_sqnc_lst.execute_sequence_list(time)
    assert len(img_sqnc_lst.sequence_list) == 2

    img_sqnc_lst.sequence.images_shown = 1
    img_sqnc_lst.execute_sequence_list(time)
    assert len(img_sqnc_lst.sequence_list) == 2

    img_sqnc_lst.sequence.images_shown = 2
    img_sqnc_lst.execute_sequence_list(time)
    assert len(img_sqnc_lst.sequence_list) == 1

    img_sqnc_lst.sequence.images_shown = 4
    assert img_sqnc_lst.execute_sequence_list(time)
