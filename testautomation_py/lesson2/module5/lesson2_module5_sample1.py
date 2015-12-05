import tempfile
import os
import os.path
import pytest


@pytest.fixture
def temp_dir(request):
    return tempfile.TemporaryDirectory()


@pytest.mark.parametrize("file_name", [
    ("test.txt"), (".txt"), ("@#$%^&"),
])
def test_create_file(temp_dir, file_name):
    test_file = os.path.join(temp_dir.name, file_name)
    open(test_file, 'tw').close()
    assert os.path.isfile(test_file)
