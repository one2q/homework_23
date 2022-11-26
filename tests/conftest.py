import pytest

from funcs import generator_from_file


@pytest.fixture()
def generator():
    yield generator_from_file('test_file.txt')