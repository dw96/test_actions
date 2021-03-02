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

    def delay(self, duration):
        """Update timestamp, then delay duration seconds before returning."""
        self.timestamp = time.time()
        wait = 0.0
        while (wait < duration):
            time.sleep(0.1)
            wait += 0.1
