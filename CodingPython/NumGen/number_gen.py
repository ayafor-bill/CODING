import random

# Common mobile prefixes (illustrative for testing)
PREFIXES = [
    "650","651","652","653","654","655","656","657",
    "670","671","672","673","674","675","676","677",
    "680","681","682","683","684","685","686","687",
    "690","691","692","693","694","695","696","697"
]

TOTAL_NUMBERS = 50_000_000
OUTPUT_FILE = "cameroon_test_numbers_no_cc.txt"

def generate_number():
    prefix = random.choice(PREFIXES)
    suffix = random.randint(100000, 999999)
    return f"{prefix}{suffix}"  # 9-digit number

with open(OUTPUT_FILE, "w") as f:
    for i in range(TOTAL_NUMBERS):
        f.write(generate_number() + "\n")
        if i % 1_000_000 == 0 and i != 0:
            print(f"{i:,} numbers generated...")

print("Done.")
