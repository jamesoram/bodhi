"""Alerters will notify the end user that a `monitor` has failed its check.
"""
import threading
import os
import time

class BlinkAlerter(threading.Thread):
    """Alerter for blink(1)
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = []
        self.command = "blink1-tool -q --rgb "
        self.blink_time = "95"

    def alert(self, monitor):
        """Alert using blink(1) with the configuration in `monitor`
        """
        self.queue.append(monitor)
        print "Error in: " + monitor.name
        os.system("blink1-tool -q --off")
        timeout = time.time() + 35
        while True:
            for i in self.queue:
                cmd = self.command + i.colour + " &"
                os.system(cmd)
                time.sleep(0.8)
                if time.time() > timeout:
                    break
        os.system("blink1-tool -q --off")
        self.queue = []

    def not_alert(self, monitor):
      print monitor.name + " OK"
      if monitor in self.queue:
          self.queue.remove(monitor)
          os.system("blink1-tool -q --off")

    def run(self):
        time.sleep(0.1)
