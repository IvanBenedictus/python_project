import os
from contextlib import contextmanager

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File("sample.txt", "w") as file:
    file.write("This is a test file")

print(file.closed)

# Using contextlib
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file("sample.txt", "w") as file:
    file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

print(file.closed)