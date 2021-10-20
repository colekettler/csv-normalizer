import csv
from datetime import datetime, timedelta, timezone
import math
import sys


def configure_encoding(encoding):
    sys.stdin.reconfigure(encoding=encoding)
    sys.stdout.reconfigure(encoding=encoding)


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

    foo_duration = normalize_duration(row["FooDuration"])
    bar_duration = normalize_duration(row["BarDuration"])
    row["FooDuration"] = foo_duration
    row["BarDuration"] = bar_duration
    row["TotalDuration"] = foo_duration + bar_duration

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


def normalize_duration(duration):
    delta = get_duration_delta(duration)
    return math.floor(delta.total_seconds())


def get_duration_delta(duration):
    units = ["hours", "minutes", "seconds", "milliseconds"]
    parts = [int(part) for part in duration.replace(".", ":").split(":")]
    kwargs = dict(zip(units, parts))
    return timedelta(**kwargs)


if __name__ == "__main__":
    configure_encoding("utf-8")
    normalize(sys.stdin)
