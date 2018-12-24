
#!/usr/bin/python3.6

from ipaddress import IPv4Network
import sys

network = sys.argv[1]
for addr in IPv4Network(network):
    print(addr)

