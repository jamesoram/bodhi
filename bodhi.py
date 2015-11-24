"""Main Bodhi module
"""
import sys
import thread
from alerters.blink_alerter import BlinkAlerter
from monitors.http_monitor import HttpMonitor
from monitors.conf_loader import ConfLoader

def main():
    """main function
    """
    if len(sys.argv) < 1:
        print "Please specify configuration file(s)"
        sys.exit(1)

    c = ConfLoader(sys.argv[1])
    c.load()
    mon = HttpMonitor(c.name, c.url, c.colour, c.poll_time, BlinkAlerter(), c.expected)
    thread.start_new_thread(mon.monitor())

if __name__ == "__main__":
    sys.exit(main())
