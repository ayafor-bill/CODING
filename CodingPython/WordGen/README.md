# WordGen - Password Generator

**Created:** May 9, 2026

## Overview

WordGen is a Python script that generates new passwords by combining existing passwords from a word list and adding randomized symbols and numbers. It reads passwords from an input file, blends them together, and outputs a set of unique password variants.

## What It Does

The script performs the following operations:

1. **Reads Input File**: Loads a list of existing passwords or words from a text file
2. **Validates Input**: Ensures at least 2 passwords exist in the file
3. **Combines Passwords**: Randomly pairs passwords and concatenates them
4. **Adds Entropy**: Appends 2-4 random symbols and numbers to each combination
5. **Filters by Length**: Keeps only passwords between 8-20 characters
6. **Deduplicates**: Stores passwords in a set to ensure uniqueness
7. **Writes Output**: Saves all generated passwords to an output file

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library `random` module)

## How to Use

### Basic Setup

1. Create an input file with your word list or passwords (one per line):

   ```bash
   cat > sidom_possible.txt << EOF
   password
   secret
   admin
   test
   example
   myword
   EOF
   ```

2. Run the script:

   ```bash
   python wordgen.py
   ```

3. Check the output file `new_passwords.txt` for generated passwords

### Custom Parameters

To change the number of passwords generated or file names, modify the script:

```python
input_file = "your_input_file.txt"
output_file = "your_output_file.txt"
generate_passwords(input_file, output_file, num_passwords=100)  # Generate 100 passwords
```

## Code Explanation

### Function Signature

```python
def generate_passwords(input_file, output_file, num_passwords=50):
```

- `input_file`: Path to file containing seed passwords
- `output_file`: Path where generated passwords will be written
- `num_passwords`: Number of unique passwords to generate (default: 50)

### File Reading

```python
with open(input_file, "r") as f:
    passwords = [line.strip() for line in f.readlines() if line.strip()]
```

Reads the input file and removes whitespace from each line, filtering out empty lines.

### Validation

```python
if len(passwords) < 2:
    print("Input file must contain at least 2 passwords.")
    return
```

Ensures sufficient diversity in the input for combining pairs.

### Password Generation Loop

```python
while len(new_passwords) < num_passwords:
    password1 = random.choice(passwords)
    password2 = random.choice(passwords)
    combined_password = password1 + password2
    extra = "".join(random.choices("1234567890!@#$%^&*", k=random.randint(2, 4)))
    combined_with_extra = combined_password + extra
    if 8 <= len(combined_with_extra) <= 20:
        new_passwords.add(combined_with_extra)
```

- Randomly selects two passwords and concatenates them
- Adds 2-4 random digits or symbols
- Only keeps results between 8-20 characters
- Uses a set for automatic deduplication

### File Writing

```python
with open(output_file, "w") as f:
    for password in new_passwords:
        f.write(password + "\n")
```

Writes each generated password on a separate line.

### Error Handling

```python
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

Catches missing files and other unexpected errors gracefully.

## Example Output

**Input file (sidom_possible.txt):**

```Words
apple
banana
cherry
dragon
```

**Generated passwords (new_passwords.txt):**

```Passwords
applebanana!@#3
cherrydragon$%^2
dragoncherrry!@1
appledragon#$%2
bananacherry@!3
```

## Limitations

### 1. Not Cryptographically Secure

The script uses Python's `random` module, which is **not** suitable for actual security-critical password generation. Use the `secrets` module for real applications.

### 2. Limited Randomness

Passwords are deterministic combinations of input words plus symbols. An attacker with the input list could potentially predict outputs.

### 3. Predictable Pattern

The combination pattern (password1 + password2 + symbols) is consistent and could be reverse-engineered.

### 4. Length Restrictions

The 8-20 character limit may reject potentially good combinations, though it helps filter unreasonable lengths.

### 5. Symbol Pool Limitations

The symbol and number pool is fixed and relatively small, limiting true entropy.

## Use Cases

This script is suitable for:

- **Test Data Generation**: Creating realistic test passwords for development/QA
- **Training Data**: Generating examples for educational purposes
- **Word List Variants**: Creating variations of base words for wordlists
- **Non-Critical Systems**: Dev/staging environment password generation

This script is **NOT** suitable for:

- Production password generation
- Real security credentials
- Systems requiring FIPS-certified randomness
- High-entropy cryptographic applications

## Improvements and Recommendations

### 1. Use `secrets` Module for Real Passwords

```python
import secrets
# Instead of: random.choices("1234567890!@#$%^&*", ...)
# Use: secrets.choice("1234567890!@#$%^&*")
```

### 2. Add Command-Line Arguments

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", default="sidom_possible.txt")
parser.add_argument("--output", default="new_passwords.txt")
parser.add_argument("--count", type=int, default=50)
```

### 3. Add Shuffling Within Words

```python
# Shuffle characters within combined password before adding symbols
shuffled = ''.join(random.sample(combined_password, len(combined_password)))
```

### 4. Add Logging

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Generated {len(new_passwords)} passwords")
```

### 5. Add Progress Bar

```python
from tqdm import tqdm
for _ in tqdm(range(num_passwords), desc="Generating passwords"):
    # generation logic
```

### 6. Add Configuration File Support

```python
import json
with open("config.json") as f:
    config = json.load(f)
    num_passwords = config.get("count", 50)
```

### 7. Better Symbol/Number Distribution

```python
# Mix symbols and numbers throughout the password, not just at the end
insert_positions = random.sample(range(len(combined_password)), k=2)
```

## Example Enhancement

Here's a more secure variant using `secrets`:

```python
import secrets

def generate_secure_passwords(input_file, output_file, num_passwords=50):
    try:
        with open(input_file, "r") as f:
            words = [line.strip() for line in f.readlines() if line.strip()]
        
        if len(words) < 2:
            print("Input file must contain at least 2 words.")
            return

        new_passwords = set()
        
        while len(new_passwords) < num_passwords:
            word1 = secrets.choice(words)
            word2 = secrets.choice(words)
            combined = word1 + word2
            
            # Better randomness for symbols/numbers
            separator = secrets.choice("!@#$%^&*-_=+")
            extra = "".join(secrets.choice("1234567890!@#$%^&*") for _ in range(3))
            
            password = combined + separator + extra
            
            if 8 <= len(password) <= 20:
                new_passwords.add(password)
        
        with open(output_file, "w") as f:
            for password in new_passwords:
                f.write(password + "\n")
        
        print(f"{len(new_passwords)} secure passwords generated.")
    except Exception as e:
        print(f"Error: {e}")
```

## Notes

- The script is suitable for educational purposes and non-critical applications
- For production use, consider more sophisticated password generation libraries
- Always test generated passwords against your system's password requirements
- Consider entropy calculations for your specific use case

## Author

Created: May 9, 2026

---

For enhancements or questions, consider implementing the recommendations above or adapting the script to your specific needs!
