from datetime import datetime
import os

def generate_log(data):

    # STEP 1: Validate input — must be a list
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # STEP 2: Generate a filename using today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write each log entry to the file (one per line)
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return the filename so callers (and tests) can reference it
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)