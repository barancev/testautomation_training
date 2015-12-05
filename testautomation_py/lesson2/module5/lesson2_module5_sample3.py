import tempfile
import os
import os.path
import shutil
import pytest
from pytest_bdd import scenario, given, when, then

@scenario('lesson2_module5_sample3.feature', 'File Creation')
def test_create_file():
    pass

@given('A directory')
def temp_dir():
    return tempfile.TemporaryDirectory()

@given('A valid <file_name>')
def valid_file_name(file_name):
    return file_name

@when('I create a file with this name in the given directory')
def create_file(temp_dir, valid_file_name):
    test_file = os.path.join(temp_dir.name, valid_file_name)
    open(test_file, 'tw').close()

@then('I should see the file created successfully')
def should_have_left_cucumbers(temp_dir, valid_file_name):
    test_file = os.path.join(temp_dir.name, valid_file_name)
    assert os.path.isfile(test_file)
