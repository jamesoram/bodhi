import sys
from alerters.blink_alerter import BlinkAlerter
from monitors.http_monitor import HttpMonitor

def main():
    mon = HttpMonitor("test", "http://localhost:31337", "hello", "DD2243", 40, BlinkAlerter())
    mon.monitor()

if __name__ == "__main__":
    sys.exit(main())
