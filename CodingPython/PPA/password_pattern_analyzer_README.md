# password_pattern_analyzer.py

This script analyzes a wordlist of passwords and reports how many entries match common weak password patterns.

## What it does

- reads a wordlist file line by line
- checks each password against predefined regex patterns
- counts matches for patterns such as:
  - word + year (e.g. `John2023`)
  - common keyboard sequences (e.g. `qwerty123`)
  - leetspeak variants of `password`
  - all-numeric passwords
  - repeated characters (e.g. `aaaaaa`)
  - word + special character combinations (e.g. `Hello@123`)
- prints the total number of matches for each pattern
- prints the 10 most common password prefixes

## Usage

Run the script and enter the path to your password wordlist when prompted:

```bash
python password_pattern_analyzer.py
```

Then provide a file path such as `wordlist.txt`.

## Purpose

This tool is useful for quickly profiling password datasets and identifying weak or predictable password construction patterns.
