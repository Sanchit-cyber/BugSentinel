class StopScan:
    def __init__(self):
        self.scanning = False

    def stop(self):
        self.scanning = False
        print("Scanning process has been halted.")