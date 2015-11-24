"""Class used for loader a monitor's configuration
"""
import json

class ConfLoader(object):
    """Create an object storing a monitor's configuration
    """
    def __init__(self, filename):
        self.filename = filename
        self.conf = None

    def load(self):
        """Load the configuration file
        """
        with open(self.filename) as conf_file:
            self.conf = json.load(conf_file)
        return self.conf
