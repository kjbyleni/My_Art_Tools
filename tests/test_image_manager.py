import pytest

from practice.image_manager import Images

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
    with pytest.raises(Exception):
        assert Images(invalid_file_path_index)


def test_invalid_folder_input():
    invalid_folder_path_index = 4
    with pytest.raises(Exception):
        assert Images(invalid_folder_path_index)

