# Word Frequency CLI

Command-line tool for counting word frequency from a text file or a URL.

## Features
- Read text from local file
- Read text from URL (http / https)
- Clean punctuation
- Case-insensitive counting
- Show TOP-N words

## Usage

python wordfreq.py book.txt<br>
python wordfreq.py book.txt --top 20<br>
python wordfreq.py https://www.gutenberg.org/files/1342/1342-0.txt
 --top 15<br>


## Example output

the: 1234<br>
and: 987<br>
to: 876<br>