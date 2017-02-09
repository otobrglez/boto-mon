#!/usr/bin/env

import re
import subprocess
import events
from os import getenv
import xml.etree.ElementTree as ET


class Scanner(object):
    def detected_events(self):
        raise Exception('Not yet implemented!')


class ArpScanner(Scanner):
    DEFAULT_ARGUMENTS = getenv('ARP_ARGUMENTS', "--interface=wlan0 --localnet")
    COMMAND = "arp-scan {}".format(DEFAULT_ARGUMENTS)

    def __init__(self, scan_arguments=None):
        if scan_arguments: self.DEFAULT_ARGUMENTS = scan_arguments

    def _scan(self):
        p = subprocess.Popen(self.COMMAND, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        return output.decode('utf-8')

    def scan(self):
        return self.process_output(self._scan())

    def process_output(self, output):
        capture = r'(\d+\.\d+\.\d+.\d+)\s([0-9a-z:]+)\s+(.*)'
        return [dict(zip(('ip', 'mac', 'vendor'), m)) for m in re.findall(capture, output)]

    def detected_events(self):
        return [events.Event(events.EventType.ArpDevicePresent, d) for d in self.scan()]


class NmapScanner(Scanner):
    DEFAULT_ARGUMENTS = getenv("NMAP_ARGUMENTS", "--host-timeout 3s -sn -T5 -oX - '192.168.168.*'")
    COMMAND = "sudo nmap {}".format(DEFAULT_ARGUMENTS)

    def __init__(self, scan_arguments=None):
        if scan_arguments: self.DEFAULT_ARGUMENTS = scan_arguments

    def _scan(self):
        p = subprocess.Popen(self.COMMAND, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        return output.decode('utf-8')

    def scan(self):
        return self.process_output(self._scan())

    def process_output(self, output):
        tree = ET.fromstring(output)
        out = []
        for host in tree.findall('.//host'):
            addresses = [address.attrib for address in host.findall('.//address')]
            details = {}

            for address in addresses:
                details[address['addrtype']] = address['addr']
                details['vendor'] = address.get('vendor', '(Unknown)')

            # Fixing ipv4 -> ip
            ip = details['ipv4']
            details.pop('ipv4', None)
            details['ip'] = ip
            out.append(details)
        return out

    def detected_events(self):
        return [events.Event(events.EventType.NmapDevicePresent, d) for d in self.scan()]


if __name__ == '__main__':
    from json import dumps

    arp_scanner = ArpScanner()
    nmap_scanner = NmapScanner()

    print(dumps({
        'arp_scan': arp_scanner.detected_events(),
        'nmap_scan': nmap_scanner.detected_events()
    }, indent=4, sort_keys=True))
