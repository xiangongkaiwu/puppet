import csv
import argparse
from pathlib import Path
import re
from chunk import chunk

parser = argparse.ArgumentParser()
parser.add_argument("chapter")
args = parser.parse_args()

raw = Path(f"chaps/Chapter{args.chapter}/raw.txt")

with raw.open("r") as f:
    text = "".join(f.readlines())

with open("glossary.txt","r") as g:
    gloss = csv.reader(g,delimiter=";")
    for row in gloss:
        text = text.replace(row[0]," " + row[1] + " ")
    text = re.sub(" +"," ",text)
    #text = text.replace("：","&&")

chunks = chunk(text, 2000)

text = "\n====================================\n\n====================================\n\n====================================\n".join(chunks)

with Path(f"chaps/Chapter{args.chapter}/glossed.txt").open("w") as f:
  f.write(text)

print(text)
