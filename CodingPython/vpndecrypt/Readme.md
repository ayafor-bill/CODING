# vpndatadec.py

## Overview

`vpndatadec.py` is a small analysis script designed to decode VPN package files and extract readable payload content. The script attempts a simple Base64 decode of the input file, preserves the decoded binary output, and collects ASCII strings that can reveal embedded configuration, URLs, or other useful data.

## Purpose

This project was born from an attempt to reverse engineer VPN files and understand their internal payloads. The goal is to inspect what is embedded inside a `.hat` VPN file so you can later analyze or modify the payload and better understand how the VPN package works.

## What it does

- Reads a VPN file as raw binary data.
- Tries to decode that data using Base64.
- Writes the decoded output to `decoded.bin`.
- Extracts readable ASCII strings from the decoded data.
- Saves those strings to `strings.txt`.

## Why this approach

Many VPN payload files include encoded or packed data. A simple Base64 decode is a common first step when investigating unknown binary files. Extracting printable ASCII strings afterward helps identify meaningful text fragments such as URLs, commands, headers, or protocol markers.

## Usage

1. Place the VPN file in the same directory as `vpndatadec.py`.
2. Run the script with Python:

```bash
python vpndatadec.py
```

1. The script creates two output files:

- `decoded.bin` — raw decoded binary output (or the original bytes if decoding fails)
- `strings.txt` — readable ASCII strings extracted from the binary

## Notes

- The script currently only performs Base64 decoding and ASCII string extraction.
- Additional analysis can be done with other reverse-engineering tools on `decoded.bin` and `strings.txt`.

## Development

This project is still in development, and community contributions are welcome. If you have ideas for better decoding methods or additional file handling, feel free to improve the script.

__Bill_

---
