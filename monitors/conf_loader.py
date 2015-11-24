"""Class used for loader a monitor's configuration
"""
import json

class ConfLoader(object):
    """Create an object storing a monitor's configuration
    """
    def __init__(self, filename):
        self.filename = filename
        self.name = None
        self.url = None
        self.colour = None
        self.poll_time = None
        self.expected = None
        self.alert_type = None

    def load(self):
        """Load the configuration file
        """
        with open(self.filename) as conf_file:
            conf = json.load(conf_file)
        self.name = conf["name"]
        self.url = conf["url"]
        self.colour = conf["colour"]
        self.poll_time = conf["poll_time"]
        self.expected = conf["expected"]
        self.alert_type = conf["alert_type"]
