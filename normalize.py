import csv
import sys


def normalize(file):
    reader = csv.reader(file)
    for row in reader:
        print(row)


if __name__ == "__main__":
    normalize(sys.stdin)
