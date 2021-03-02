"""Test example Python class.

Christian Angelsen, STFC Detector Systems Software Group
"""
import time


class Example():
    """Test class."""

    def __init__(self):
        """Initialize the object."""
        self.string = ""
        self.timestamp = 0

    def lowercase(self, string):
        """Turn string into lower case letters."""
        self.string = string.lower()

    def stamp_timestamp(self):
        """Update timestamp."""
        self.timestamp = time.time()
