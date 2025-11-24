import csv

input_path = "all_reviews.csv"
output_path = "final_clean.csv"

EXPECTED_COLS = 19

with open(input_path, "r", encoding="utf-8", errors="replace") as infile, \
     open(output_path, "w", encoding="utf-8", newline="") as outfile:

    writer = csv.writer(outfile)

    for line in infile:
        # Fix broken quotes
        cleaned = line.replace('\\"', '"')

        # Split ONLY on commas that are not inside quotes
        parts = next(csv.reader([cleaned], skipinitialspace=True))

        # Keep only rows with expected column count
        if len(parts) == EXPECTED_COLS:
            writer.writerow(parts)
