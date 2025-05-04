import csv
import argparse
from pathlib import Path
import re
from chunk import chunk
import pyperclip

text = pyperclip.paste()

with open("glossary.txt","r") as g:
    gloss = csv.reader(g,delimiter=";")
    for row in gloss:
        if len(row[0]) != 1 or row[0] == '妖':
            text = text.replace(row[0]," " + row[1] + " ")
    text = re.sub(" +"," ",text)
    text = text.replace("\r\n\r\n","\n")
    #text = text.replace("：","&&")

chunks = chunk(text, 3000)

for i in range(len(chunks)):
  chunks[i] = "Translate the following chunk of a chapter of a xianxia novel. The words in English should remain directly in English. Avoid using dashes of any kind (including but not limited to en dashes and em dashes) if they are not explicitly in the provided text. Do not bold, italicize, or underline any text. \n\n" + chunks[i]

text = "\n====================================\n\n====================================\n\n====================================\n".join(chunks)

print(text)
