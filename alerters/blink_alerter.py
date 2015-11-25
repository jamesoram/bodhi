"""Alerters will notify the end user that a `monitor` has failed its check.
"""
import threading
import os
import Queue
import time

class BlinkAlerter(threading.Thread):
    """Alerter for blink(1)
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = [] #Queue.LifoQueue()
        self.command = "blink1-tool --rgb "
        self.blink_time = "95"
        self.engaged = False

    def alert(self, monitor):
        """Alert using blink(1) with the configuration in `monitor`
        """
        self.queue.append(monitor)
        if self.engaged == False:
            self.engaged = True
            print "Error in: " + monitor.name
            cmd = self.command + self.queue.pop().colour + " -q --blink " + self.blink_time
            os.system(cmd + "&")
        else:
            os.system("blink1-tool --off")
            for i in range(1, 10):
                cmd = self.command + self.queue.pop().colour
                os.system(cmd)
                time.sleep(400)
                os.system("blink1-tool --off")
        self.engaged = False
