import sys

def main():
    mon = HttpMonitor("test", "http://localhost:31337", "hello", "DD2243", 40, BlinkAlerter())
    mon.monitor()

if __name__ == "__main__": 
    sys.exit(main())
