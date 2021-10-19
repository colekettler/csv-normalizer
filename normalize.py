import csv
from datetime import datetime, timedelta, timezone
import sys


def normalize(file):
    reader = csv.DictReader(file)
    writer = csv.DictWriter(sys.stdout, fieldnames=reader.fieldnames)

    writer.writeheader()
    for row in reader:
        writer.writerow(normalize_row(row))


def normalize_row(row):
    row["Timestamp"] = normalize_timestamp(row["Timestamp"])
    row["ZIP"] = normalize_zip(row["ZIP"])
    row["FullName"] = normalize_full_name(row["FullName"])
    return row


def normalize_timestamp(timestamp):
    format = "%m/%d/%y %I:%M:%S %p"
    dt_pst = datetime.strptime(timestamp, format)

    est_offset = 3
    dt_est = dt_pst + timedelta(hours=est_offset)

    est_tz = timezone(timedelta(hours=-5))
    dt_est_with_tz = dt_est.replace(tzinfo=est_tz)

    return dt_est_with_tz.isoformat()


def normalize_zip(zip_code):
    return zip_code.zfill(5)


def normalize_full_name(name):
    return name.upper()


if __name__ == "__main__":
    normalize(sys.stdin)
