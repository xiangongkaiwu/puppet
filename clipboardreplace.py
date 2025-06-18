import csv
import argparse
from pathlib import Path
import re
from chunk import chunk
import clipman as pyperclip

pyperclip.init()

text = pyperclip.paste()

with open("glossary.txt","r") as g:
    gloss = csv.reader(g,delimiter=";")
    for row in gloss:
        text = text.replace(row[0]," " + row[1] + " ")
    text = re.sub(" +"," ",text)
    text = text.replace("\r\n\r\n","\n")
    #text = text.replace("：","&&")

chunks = chunk(text, 5000)

text = "\n====================================\n\n====================================\n\n====================================\n".join(chunks)

print(text)
