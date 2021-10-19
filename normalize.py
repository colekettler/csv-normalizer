import csv
from datetime import datetime, timedelta
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
    dt_pst = datetime.strptime(timestamp, format)

    est_offset = 3
    dt_est = dt_pst + timedelta(hours=est_offset)

    return dt_est.isoformat()


if __name__ == "__main__":
    normalize(sys.stdin)
