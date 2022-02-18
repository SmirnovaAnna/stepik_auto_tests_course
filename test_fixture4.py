import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def prepare_faces():
    """Output emoticons ^_^ and :3

    :return: empty generator
    """
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    """Output emoticons :)

    :return: None
    """
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    """Output emoticon :-Р

    :return: None
    """
    print(":-Р", "\n")


class TestPrintSmilingFaces():
   def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
    """Output emoticons ^_^, :3 and :)

    :return: None
    """
    print()
# какие-то проверки

   def test_second_smiling_faces(self, prepare_faces):
    """Output emoticons ^_^ and :3

    :return: None
    """
    print()
# какие-то проверки