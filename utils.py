import os


def template(directory, file_name):
    return os.path.join(os.path.dirname(__file__), directory, file_name)