# RevStr - String Reverser

**Created:** May 9, 2026

## Overview

A simple C program that reads input from stdin and outputs it reversed.

## Usage

Compile:

```bash
gcc revstr.c -o revstr
```

Run:

```bash
echo "hello world" | ./revstr
# Output: dlrow olleh
```

## Requirements

- GCC compiler
- Standard C libraries (stdio.h, string.h)

## Notes

- Reads until EOF
- Preserves all characters including spaces
- Max input length: 999 characters
