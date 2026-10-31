import argparse,hashlib,json
from pathlib import Path
def sha256(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for chunk in iter(lambda:f.read(65536),b""):h.update(chunk)
 return h.hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument("paths",nargs="+");a.add_argument("--manifest",default="manifest.json");x=a.parse_args()
 data={str(p):sha256(p) for p in x.paths if Path(p).is_file()}
 Path(x.manifest).write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8");print(json.dumps(data,indent=2))
if __name__=="__main__":main()
