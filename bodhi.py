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
    alerter = BlinkAlerter()
    conf_files = [f for f in sys.argv if ".json" in f]
    for conf_file in conf_files:
        c = ConfLoader(conf_file)
        c.load()
        mon = HttpMonitor(c.name, c.url, c.expected, c.colour, c.poll_time, alerter)
        thread.start_new_thread(mon.monitor())

if __name__ == "__main__":
    sys.exit(main())
