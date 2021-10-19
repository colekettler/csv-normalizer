import csv
from datetime import datetime
import sys


def normalize(file):
    reader = csv.reader(file)
    writer = csv.writer(sys.stdout)

    for row in reader:
        writer.writerow(normalize_row(row))


def normalize_row(row):
    return row


def normalize_timestamp(timestamp):
    format = "%m/%d/%y %I:%M:%S %p"
    return datetime.strptime(timestamp, format).isoformat()


if __name__ == "__main__":
    normalize(sys.stdin)
