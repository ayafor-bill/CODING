import random

def generate_passwords(input_file, output_file, num_passwords=50):
    try:
        # Read existing passwords from the input file
        with open(input_file, "r") as f:
            passwords = [line.strip() for line in f.readlines() if line.strip()]
        
        # Check if there are enough passwords
        if len(passwords) < 2:
            print("Input file must contain at least 2 passwords.")
            return

        # Create a set to store unique new passwords
        new_passwords = set()

        # Generate passwords
        while len(new_passwords) < num_passwords:
            # Randomly select two passwords
            password1 = random.choice(passwords)
            password2 = random.choice(passwords)

            # Combine the entire passwords
            combined_password = password1 + password2

            # Add symbols and numbers
            extra = "".join(random.choices("1234567890!@#$%^&*", k=random.randint(2, 4)))
            combined_with_extra = combined_password + extra

            # Ensure reasonable length (between 8 and 20 characters)
            if 8 <= len(combined_with_extra) <= 20:
                new_passwords.add(combined_with_extra)

        # Write the new passwords to the output file
        with open(output_file, "w") as f:
            for password in new_passwords:
                f.write(password + "\n")

        print(f"{len(new_passwords)} new passwords generated and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = "sidom_possible.txt"  # Input file containing old passwords
output_file = "new_passwords.txt"  # File to store new passwords
generate_passwords(input_file, output_file)