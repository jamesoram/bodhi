import urllib2
import time
import Queue
import os
import threading 
import sys

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

class BlinkAlerter(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = Queue.LifoQueue()
        self.command = "blink1-tool --rgb "
        self.blink_time = "95"

    def alert(self, monitor):
        self.queue.put(monitor)
        print "Error in: " + monitor.name
        cmd = self.command + self.queue.get().colour + " -q --blink " + self.blink_time
        os.system(cmd)

def main():
    mon = HttpMonitor("test", "http://localhost:31337", "hello", "DD2243", 40, BlinkAlerter())
    mon.monitor()

if __name__ == "__main__": 
    sys.exit(main())
