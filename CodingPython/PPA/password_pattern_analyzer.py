import re
from collections import Counter

def analyze_password_patterns(wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.read().splitlines()
    
    patterns = {
        "Word + Year (e.g., John2023)": re.compile(r"^[A-Za-z]+(19|20)\d{2}$"),
        "Common Keyboard Patterns (e.g., qwerty123)": re.compile(r"^(qwerty|asdf|zxcvbn|123456|password)\d*$"),
        "Leetspeak Variations (e.g., P@ssw0rd)": re.compile(r"^[Pp@]{1}[aA4]{1}[sS5]{2}[wW]{1}[oO0]{1}[rR]{1}[dD]$"),
        "Only Numbers (e.g., 12345678)": re.compile(r"^\d+$"),
        "Repeated Characters (e.g., aaaaaa, 111111)": re.compile(r"^(.)\1+$"),
        "Word + Special Characters (e.g., Hello@123)": re.compile(r"^[A-Za-z]+[@#$%^&*!]+[0-9]*$")
    }

    matches = {key: 0 for key in patterns}

    for password in passwords:
        for pattern_name, pattern in patterns.items():
            if pattern.match(password):
                matches[pattern_name] += 1

    print("\n🔹 **Password Pattern Analysis:**\n")
    for pattern, count in matches.items():
        print(f"{pattern}: {count} matches")

    # Show the most common password prefixes
    common_prefixes = Counter([p[:4] for p in passwords if len(p) > 4])
    print("\n🔹 **Most Common Password Prefixes:**")
    for prefix, count in common_prefixes.most_common(10):
        print(f"{prefix}: {count} occurrences")

if __name__ == "__main__":
    wordlist_path = input("Enter path to the wordlist file: ")
    analyze_password_patterns(wordlist_path)