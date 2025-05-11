import tkinter as tk
from ui.interface import UserInterface
from scanner.subdomain_finder import SubdomainFinder
from scanner.vulnerability_scanner import VulnerabilityScanner
from scanner.stop_scan import StopScan

class BugHuntingTool:
    def __init__(self):
        self.ui = UserInterface()
        self.subdomain_finder = SubdomainFinder()
        self.vulnerability_scanner = VulnerabilityScanner()
        self.stop_scan = StopScan()
        self.running = False

    def run(self):
        self.ui.display_warning()
        url = self.ui.prompt_user_input()
        if url:
            self.start_scanning(url)

    def start_scanning(self, url):
        self.running = True
        subdomains = self.subdomain_finder.find_subdomains(url)
        self.ui.show_vulnerabilities(subdomains)

        # Example of scanning for vulnerabilities
        if self.running:
            vulnerabilities = self.vulnerability_scanner.scan_all_vulnerabilities(url, subdomains)
            self.ui.show_vulnerabilities(vulnerabilities)

    def stop(self):
        self.running = False
        self.stop_scan.stop()

if __name__ == "__main__":
    tool = BugHuntingTool()
    tool.run()
