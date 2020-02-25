import os
from contextlib import contextmanager

class Openfile():

    def __init__(self, filename, mode):
        print("__init__ called...")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("__enter__ called...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        print("__exit__ called...")
        self.file.close()

print("Example 1: Context Manager using generator function...")

with Openfile("./Data/Sample.txt", "w") as f:
    print("Writing to the file...")
    f.write("Testing 1....")

print("Is file closed = {}".format(f.closed))


print("\nExample 2: Context Manager using @contextmanager")

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file("./Data/Sample.txt", "w") as f:
    print("Writing to the file...")
    f.write("Testing 2....")

print("Is file closed = {}".format(f.closed))


print("\nExample 3: Context Manager using @contextmanager")

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir("./Data"):
    print(os.listdir())
