import base64, re, zlib, binascii
from pathlib import Path

data = Path("HA VIP.hat").read_bytes()

try:
    decoded = base64.b64decode(data)
except:
    decoded = data

# Save decoded binary
Path("decoded.bin").write_bytes(decoded)

# Extract readable ASCII strings
strings = re.findall(rb"[ -~]{4,}", decoded)
with open("strings.txt", "wb") as f:
    f.write(b"\n".join(strings))

print("[✓] Saved decoded binary and strings.txt")