"""
Basic unit test for the image hasher program.
Run using pytest from the command line, e.g.: `pytest test_gather_image_hashes.py`
"""
import json
import pathlib

from gather_image_hashes import ImageHasher


def test_gather_image_hashes():
    """
    Basic test to confirm that our program provides the correct result given the images in the 
    example_images directory.
    """
    # Arrange
    cur_dir = pathlib.Path(__file__).parent.resolve()
    with open(f"{cur_dir}/test_expected_output.txt", encoding="utf-8") as file:
        raw_data = file.read()
    expected_output = json.loads(raw_data)
    hasher = ImageHasher(f"{cur_dir}/example_images")

    # Act
    actual_result = hasher.main()

    # Assert
    assert len(actual_result) == len(expected_output)
    for key, value in actual_result.items():
        assert sorted(expected_output[key]) == sorted(value)
