from scapy.all import *
import ipaddress

# What scapy does? It breaks the pakcet into layers and makes it easy to access the various packet fields at each layer
# Layers in scapy are specified as classes

ports = [21,25,53,433,455,8080,8443]

#SYN Scanning Function
        # Initializing the IP and TCP Layers of the packet
        # sr stands for send/receive
        # answered syn packets are stored in ans while unanswered are stored in unans
def SynScan(host):
    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=port,flags="S")
        ,timeout=2, verbose=0)
    print("Open Ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)

#DNS scanning Function        
def DNSScan(host):
    ans,unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,gd=DNSQR (qname="google.com"))
        ,timeout=2, verbose=0
    )
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)
        
host = input("Enter IP Address: ")
try:
    ipaddress.ip_address(host)
    SynScan(host)
    DNSScan(host)

except:
    print("Invalid Address")
    exit(-1)