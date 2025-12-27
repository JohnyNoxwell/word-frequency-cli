# Word Frequency CLI

Command-line tool for counting word frequency from a text file or a URL.

## Features

- Read text from local file
- Read text from URL (http / https)
- Clean punctuation
- Case-insensitive counting
- Show TOP-N words

## Usage

python wordfreq.py book.txt
python wordfreq.py book.txt --top 20
python wordfreq.py https://www.gutenberg.org/cache/epub/1342/pg1342.txt --top 15

## Setup

python -m venv venv

Activate it on Windows:
venv\Scripts\activate

Activate it on macOS / Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the tool:
python wordfreq.py book.txt --top 20

## Example output

the: 1234
and: 987
to: 876
of: 765
