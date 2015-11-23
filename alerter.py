import threading
import os
import Queue

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
