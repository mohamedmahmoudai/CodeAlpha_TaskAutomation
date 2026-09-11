import os
import re

def extract_emails(input_file_path, output_file_path):
    # Regex pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Check if input file exists; if not, create a sample file for testing
    if not os.path.exists(input_file_path):
        print(f"⚠️ Notice: '{input_file_path}' not found. Creating a test sample file...")
        with open(input_file_path, "w", encoding="utf-8") as sample_file:
            sample_file.write("Hello, contact us at support@codealpha.tech or info@example.com for queries.\n")
            sample_file.write("For urgent requests, email mohamed.dev@domain.org or support@codealpha.tech.")
        print(f"📄 Sample file created successfully: '{input_file_path}'\n")

    try:
        # Read text content
        with open(input_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Find all emails and extract unique ones
        found_emails = re.findall(email_pattern, content)
        unique_emails = sorted(list(set(found_emails)))

        print(f"🔍 Found {len(unique_emails)} unique email address(es):")
        for email in unique_emails:
            print(f" • {email}")

        # Save results to output file
        with open(output_file_path, "w", encoding="utf-8") as out_file:
            out_file.write("--- Extracted Email Addresses ---\n")
            for email in unique_emails:
                out_file.write(f"{email}\n")

        print(f"\n✅ Successfully exported extracted emails to '{output_file_path}'")

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    print("========================================")
    print("   CodeAlpha Task Automation Script     ")
    print("========================================\n")
    
    input_file = "sample_text.txt"
    output_file = "extracted_emails.txt"
    
    extract_emails(input_file, output_file)
