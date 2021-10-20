# csv-normalizer

A CLI application to normalize a CSV provided via `stdin` and write it to `stdout`.

## Requirements

* Python 3.7+

## Usage

To normalize `sample.csv` and output it to `output.csv`:

```#bash
python3 normalize.py < sample.csv > output.csv
```

## Testing

To install dependencies for and run the test suite for this application:

```#bash
pip install -r requirements.txt
pytest
```
