import urllib2
import time

class HttpMonitor(object):

    def __init__(self, name, url, expected, colour, poll_time, alerter):
        self.name = name
        self.url = url
        self.expected = expected
        self.colour = colour
        self.poll_time = poll_time
        self.running = True
        self.alerter = alerter

    def check(self):
        ok = True
        try:
            response = urllib2.urlopen(self.url).read()
        except urllib2.URLError:
            response = ""
        if not self.expected in response:
            ok = False
        if not ok:
            self.alerter.alert(self)

    def monitor(self):
        while self.running:
          self.check()
          time.sleep(self.poll_time)
