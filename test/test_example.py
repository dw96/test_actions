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

    def test_example_delay(self):
        """Test function timestamps member viable then waits delay seconds."""
        current_timestamp = time.time()
        self.test_example.example.stamp_timestamp()
        example_timestamp = self.test_example.example.timestamp()
        assert pytest.approx(example_timestamp) == current_timestamp
