# number_gen.py

This script generates a large list of random 9-digit numbers using a set of mobile number prefixes. It is designed to produce test data quickly and write it to a text file.

## What it does

- chooses a random prefix from a predefined list
- generates a random 6-digit suffix for each number
- combines them into a 9-digit string
- writes the result to `cameroon_test_numbers_no_cc.txt`
- prints progress messages every 1,000,000 numbers

## Use cases

This script can be useful for generating sample phone-number data for testing and development purposes, such as:

- validating data import workflows
- populating test datasets for analytics or simulations
- exercising input handling in applications that accept phone numbers

## Important ethical notice

Any bulk data generation should only be used on systems you own or are explicitly authorized to test. Do not use generated numbers to perform credential stuffing, unauthorized access, or attacks against third-party services. Always follow applicable laws and responsible disclosure policies when performing security testing.
