"""Monitors that can potentially trigger an alert
"""
import urllib2
import time
import threading

class HttpMonitor(threading.Thread):
    """Monitor for HTTP calls.
    """
    def __init__(self, name, url, expected, colour, poll_time, alerter):
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        self.expected = expected
        self.colour = colour
        self.poll_time = poll_time
        self.running = True
        self.alerter = alerter

    def check(self):
        """Check to see if the HTTP call contains the expected string
        """
        response_ok = True
        try:
            print time.asctime(time.localtime(time.time())) + " Polling " + self.name
            response = urllib2.urlopen(self.url).read()
        except urllib2.URLError:
            response = ""
        if not self.expected in response:
            response_ok = False
        if not response_ok:
            self.alerter.alert(self)

    def run(self):
        """Monitor as configured.
        """
        while self.running:
            self.check()
            time.sleep(self.poll_time)
