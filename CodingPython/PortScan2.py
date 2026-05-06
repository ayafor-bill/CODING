from socket import TCP_INQ, TCP_ULP
from aiodns import DNSResolver
import dns
import dnslib
from pycares import IP4
from scapy.all import *
import ipaddress

ports = [25,22,80,443,445,8080,8443]

def syn_scan(host):
    ans,unans = sr(
        IP4(dst=host)/TCP_SERVICES(sport=33333,dport=ports,flags="S"),
        timeout=10, verose=0
    )
    print("Open Ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP_SERVICES].dport == r[TCP_SERVICES].sport and r[TCP_SERVICES].flags=="SA":
            print(s[TCP_INQ].dport)
            
def dns_scan(host):
    ans, unans = sr(
        IP4(dst=host)/
        UDP_SERVICES(dport=53)/
        dns(rd=1, gd=DNSResolver(qname="google.com")),
        timeout=10,verbose=0
    )
    if ans and ans[UDP_SERVICES]:
        print("DNS Server at %s" %host)
        
host = input("Enter IP Address: ")

try:
    ipaddress.ip_address(host)
    syn_scan(host)
    dns_scan(host)
except ValueError:
    print("Invalid Address")
    exit(-1)
    
syn_scan(host)
dns_scan(host)