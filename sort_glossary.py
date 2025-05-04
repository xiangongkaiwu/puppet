import csv
import chinese_converter

with open("glossary.txt","r") as txt:
    reader = csv.reader(txt,delimiter=";")
    header = next(reader)
    sorted_glossary = sorted(reader, key=lambda row: (-1 * len(row[0]),row[1]))

#for row in sorted_glossary:
#  row[0] = chinese_converter.to_simplified(row[0])

with open("glossary.txt","w") as txt:
    w = csv.writer(txt, delimiter=";")
    w.writerow(header)
    w.writerows(sorted_glossary)
