# RevStr - String Reversal Tool

**Created:** May 9, 2026

## Overview

RevStr is a simple Python script that reverses any string input by the user. It demonstrates the use of Python's slice notation and basic I/O operations, making it an excellent learning tool for beginners exploring string manipulation.

## What It Does

The script performs a single, straightforward operation:

1. **Prompts for Input**: Displays "Enter a word: " and waits for user input
2. **Reverses the String**: Uses Python's slice notation to reverse the input string
3. **Displays Output**: Prints the reversed string to the console

## Requirements

- Python 3.x
- No external dependencies (uses only built-in Python functions)

## How to Use

### Running the Script

Execute the script from the command line:

```bash
python revstr.py
```

### Interactive Usage

The script will prompt you to enter a word:

```text
Enter a word: hello
olleh
```

### More Examples

```text
Enter a word: python
nohtyp

Enter a word: programming
gnimmargorP

Enter a word: racecar
racecar
```

## Code Explanation

### Input Capture

```python
word = input("Enter a word: ")
```

The `input()` function displays the prompt "Enter a word: " and waits for the user to type something. It returns the user's input as a string and stores it in the variable `word`.

### String Reversal

```python
print(word[::-1])
```

This line uses Python's slice notation to reverse the string and print it immediately. The syntax `[::-1]` means:

- Empty start position: begin at the end (when step is negative)
- Empty stop position: continue to the beginning (when step is negative)
- `-1` step: move backward through the string one character at a time

## How Slice Notation Works

Python slice notation follows the pattern: `[start:stop:step]`

**For string reversal `[::-1]`:**

| Component | Value | Meaning |
| --- | --- | --- |
| start | (omitted) | Defaults to the end when step is negative |
| stop | (omitted) | Defaults to the beginning when step is negative |
| step | -1 | Move backward through the string |

**Visualizing the process:**

Original string: `"hello"`

```text
h  e  l  l  o     (forward indices: 0, 1, 2, 3, 4)
o  l  l  e  h     (after [::-1])
```

## Equivalent Approaches

While `[::-1]` is the most Pythonic way, here are alternative methods:

### Using `reversed()`

```python
word = input("Enter a word: ")
print(''.join(reversed(word)))
```

### Using a Loop

```python
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(reversed_word)
```

### Using Recursion

```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

word = input("Enter a word: ")
print(reverse_string(word))
```

## Why `[::-1]` is Best

- **Concise**: Single, readable line of code
- **Efficient**: Uses optimized C implementation under the hood
- **Pythonic**: Idiomatic Python style preferred by the community
- **Clear Intent**: Immediately recognizable as string reversal to experienced Python developers

## Common Use Cases

### Palindrome Checking

```python
word = input("Enter a word: ")
reversed_word = word[::-1]
if word.lower() == reversed_word.lower():
    print("It's a palindrome!")
else:
    print("Not a palindrome")
```

### DNA Sequence Complement (Biology)

```python
# Reverse and complement DNA sequences
dna = "ATCG"
complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
result = ''.join(complement[base] for base in dna[::-1])
print(result)  # Output: CGAT
```

### Text Encryption (Simple)

```python
# Basic reversal cipher
plaintext = input("Enter text: ")
ciphertext = plaintext[::-1]
print("Encrypted:", ciphertext)
```

## Extensions and Improvements

### 1. Add Input Validation

```python
word = input("Enter a word: ")
if word:
    print(word[::-1])
else:
    print("Please enter a valid word.")
```

### 2. Handle Multiple Reversals

```python
while True:
    word = input("Enter a word (or 'quit' to exit): ")
    if word.lower() == 'quit':
        break
    print(word[::-1])
```

### 3. Case Preservation

```python
word = input("Enter a word: ")
reversed_word = word[::-1]
print(reversed_word)
# Original case is automatically preserved
```

### 4. Statistics

```python
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"Original: {word}")
print(f"Reversed: {reversed_word}")
print(f"Length: {len(word)} characters")
print(f"Is palindrome: {word.lower() == reversed_word.lower()}")
```

### 5. File-Based Processing

```python
def reverse_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            f.write(line.strip()[::-1] + '\n')

reverse_file('input.txt', 'output.txt')
```

## Learning Outcomes

This script teaches:

1. **User Input**: How to capture user input with `input()`
2. **String Slicing**: Understanding Python's slice notation
3. **Step Values**: How negative step values reverse sequences
4. **Output**: Printing results with `print()`
5. **String Indexing**: How Python accesses string characters

## Performance Considerations

For most practical purposes, `[::-1]` is extremely efficient:

- **Time Complexity**: O(n) where n is the string length
- **Space Complexity**: O(n) for creating the reversed copy
- **Optimization**: Uses optimized C code under the hood

For extremely large strings (millions of characters), the performance difference is negligible.

## Common Mistakes

### 1. Forgetting the Colon

```python
# WRONG: word[-1::-1]  (starts from last character)
# CORRECT: word[::-1]
```

### 2. Using `reverse()` (for lists)

```python
# WRONG: word.reverse()  (strings don't have this method)
# CORRECT: word[::-1]
```

### 3. Over-complicating

```python
# WRONG: ''.join([word[i] for i in range(len(word)-1, -1, -1)])
# CORRECT: word[::-1]
```

## Palindromes

Palindromes are words that read the same forwards and backwards. This script is perfect for identifying them:

```python
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
```

**Examples of palindromes:**

- racecar
- madam
- radar
- level
- noon
- civic

## Notes

- The script preserves case (uppercase/lowercase)
- It works with any string, not just single words
- Special characters and spaces are also reversed
- The original string remains unchanged (strings are immutable)

## Author

Created: May 9, 2026

---

This simple script is a great introduction to Python string manipulation. Feel free to extend it with the suggestions above or use it as a building block for more complex projects!
