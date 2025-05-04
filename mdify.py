import os
from pathlib import Path

p = Path("/mnt/c/Users/felix/Documents")
b = Path("/mnt/c/Users/felix/Documents/PuppetMasterChaps")

for fi in p.glob("pmch*.odt"):
  os.system(f"odt2txt {fi.resolve().as_posix()} > {b.resolve()}/{fi.stem}.md")

for fi in b.iterdir():
  with fi.open() as f:
    content = f.read()
    content = content.replace("\n\n","%%").replace("\n"," ").replace("%%","\n\n");
  with fi.open("w") as f:
    f.write(content)
