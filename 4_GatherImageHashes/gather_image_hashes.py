"""
This module provides the functionality to calculate the sha256 hashes of all images in a given
directory and return dictionary with a key of the hash string and a value which is a list of
file paths for images with that hash.
Any value larger than 1 in the dictionary means that there are duplicate images.
"""

import hashlib
import os
import queue
from threading import Thread


MAX_THREADS = 8 # choose 8 threads max because my computer has 8 performance cores.


class ImageHasher:
    """
    Class to handle the threading and queing of the application to process images as quickly as
    possible.
    """
    def __init__(self, path_to_image_dir: str) -> None:
        """
        Note: path_to_file must be an absolute path to the file, in string format.
        """
        self.path_to_image_dir = path_to_image_dir
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.threads = [Thread(target=self.calculate_hash) for _ in range(MAX_THREADS)]

    def main(self) -> dict:
        """
        Main function which takes a path to a directory on the local machine (absolute path)
        that contains a number of images. This function calculates the sha256 hash of each image in
        the path_to_image_dir and returns a dictionary with a key of the hash string and a value
        which is a list of file paths for images with that hash.
        """
        result = {}
        files = [f"{self.path_to_image_dir}/" +
                 image for image in os.listdir(self.path_to_image_dir)]
        for item in files:
            self.input_queue.put(item)
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        print("\n")
        while not self.output_queue.empty():
            item = self.output_queue.get()
            sha256 = item[0]
            file = item[1]
            if sha256 in result:
                result[sha256].append(file)
                print(f"There is at least one duplicate of {file}")
            else:
                result[sha256] = [file]
        return result

    def calculate_hash(self) -> None:
        """
        Simple method to generate the hash of a given file.
        """
        while not self.input_queue.empty():
            path_to_file = self.input_queue.get()
            sha256_hash = hashlib.sha256()
            # Read and update hash string value in blocks of 4K
            for byte_block in self.__read_image_file_generator(path_to_file):
                sha256_hash.update(byte_block)
            self.output_queue.put((sha256_hash.hexdigest(), path_to_file))

    def __read_image_file_generator(self, path_to_file: str) -> str:
        """
        Simple generator to yield portions of the file at a time without loading the whole
        image into memory at once.
        """
        with open(path_to_file,"rb") as file:
            for byte_block in iter(lambda: file.read(4096),b""):
                yield byte_block
