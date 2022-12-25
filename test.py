import os
import glob
import tqdm
import json

""""
# solution 1
jsObj = json.dumps(name_emb)
with open(emb_filename, "w") as f:
    f.write(jsObj)
    f.close()
"""


#file_name = "./data/sample.json"
file_name = "./data/twords.json"

#files = glob.glob("./data/sample.json")
#print(files)
num_uttr = 2
with open(file_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    print(len(lines))
    for i in range(0, len(lines), 1):
        sentences = lines[i]
        print(sentences)