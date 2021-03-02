"""Test Cases for example.py.

Christian Angelsen, STFC Detector Systems Software Group
"""

from example import Example
import unittest
import pytest
import time


class ExampleTestFixture(object):
    """Test fixture class."""

    def __init__(self):
        """Initialise object."""
        self.example = Example()


class TestAdapter(unittest.TestCase):
    """Unit tests for the Example class."""

    def setUp(self):
        """Set up test fixture for each unit test."""
        self.test_example = ExampleTestFixture()

    def test_example_lowercase(self):
        """Test lowercase function."""
        self.test_example.example.lowercase("hEllO")
        assert self.test_example.example.string == "hello"

    # def test_adapter_get_fp_adapter(self):
    #     """Test that a call to the detector adapter's GET method returns the correct response."""
    #     # Hack: Initialise adapters in adapter.py
    #     self.test_adapter.adapter.adapters = self.test_adapter.adapters

    #     expected_response = {
    #         'frames_written': 0,
    #         'frames_processed': 0,
    #         'writing': True
    #     }
    #     response = self.test_adapter.adapter.get(
    #         "fp/",
    #         self.test_adapter.request)
    #     assert response.status_code == 200
    #     assert expected_response == response.data['value'][0]['hdf']
