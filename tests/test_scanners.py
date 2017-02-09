import unittest
from scanners import ArpScanner, NmapScanner
from json import loads, dumps
from pprint import pprint
from os import path


class ArpScannerTestCase(unittest.TestCase):
    scanner = None

    def setUp(self):
        self.scanner = ArpScanner()
        self.scanner.scan = self.scan_from_file

    def scan_from_file(self):
        scan_file = 'static/arp_scanner_scan.json'
        with open(path.join(path.dirname(__file__), scan_file), 'r') as f: content = f.read()
        return loads(content, encoding='utf-8')

    def test_detect_events(self):
        events = self.scanner.detected_events()
        self.assertEqual(len(events), 15)


class NmapScannerTestCase(unittest.TestCase):
    scanner = None

    def setUp(self):
        self.scanner = NmapScanner()
        self.scanner._scan = self.scan_from_file

    def scan_from_file(self):
        scan_file = 'static/nmap_root_scan.xml'
        with open(path.join(path.dirname(__file__), scan_file), 'r') as f: content = f.read()
        return content

    def test_detect_events(self):
        events = self.scanner.detected_events()
        self.assertEqual(len(events), 18)


if __name__ == '__main__':
    unittest.main()
