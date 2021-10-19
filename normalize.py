import csv
import sys


def normalize(file):
    reader = csv.reader(file)
    writer = csv.writer(sys.stdout)

    for row in reader:
        writer.writerow(row)


if __name__ == "__main__":
    normalize(sys.stdin)
