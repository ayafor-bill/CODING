# PortScan.py

A network scanning script that uses Scapy to perform SYN scanning and DNS detection on target hosts.

## What it does

- **SYN Scan**: sends TCP SYN packets to a list of common ports and detects which are open
- **DNS Scan**: checks if the host is running a DNS server on port 53
- validates the input IP address before scanning
- reports open ports and active services

## Requirements

Install Scapy:

```bash
python -m pip install scapy
```

## How to use

Run the script and enter a target IP address when prompted:

```bash
python PortScan.py
```

```Example:
Enter IP Address: 192.168.1.1
```

## How it works

- The script sends TCP SYN packets with `flags="S"` to ports like 21, 25, 53, 433, 455, 8080, and 8443
- It listens for replies: if the target responds with a SYN-ACK (`flags=="SA"`), the port is open
- It also attempts a DNS query to detect if the host is running a DNS server
- Valid responses indicate open services

## Important Notes

- **Use only on networks and systems you own or have explicit permission to test**
- Do not use this on systems you don't have authorization to scan
- Some networks may block or throttle ICMP and UDP traffic
- Scapy may require elevated privileges on some systems to send raw packets

## Known Issues

The current code has several bugs that need fixing:

1. `SynScan()` references `port` but never loops over the `ports` list
2. The DNS query has a typo: `gd=DNSQR` should be `qd=DNSQR`
3. Space in `DNSQR (` should be removed
