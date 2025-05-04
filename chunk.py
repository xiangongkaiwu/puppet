from pathlib import Path
import argparse

chunksize = 3000

def chunk(text, size):
  chunks = []
  t = ""
  for line in text.split("\n"):
    if len(line) + len(t) > size:
      chunks.append(t)
      t = line + "\n"
    else:
      t += line + "\n"
  chunks.append(t + "\n")
  return chunks

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("filename")
  args = parser.parse_args()
  with open(f"{args.filename}") as f:
    text = "".join(f.readlines())
  chunks = chunk(text, chunksize)
  for i, chunk in enumerate(chunks):
    with (Path(args.filename).parent / f"chunk{i}.txt").open("w") as f:
      f.write(chunk)
