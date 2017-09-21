from datetime import datetime
from dateutil.parser import parse
import os
folder = r"C:\Users\CCrowe\Documents\Modern Software Methodologies\Quiz 1\Files"
paths = [os.path.join(folder,"A01.txt"),
        os.path.join(folder,"A02.txt"),
        os.path.join(folder,"A03.txt")]
slides = []
def ContainsDate(line):
    spl = line.split()
    for x in spl:
        try:
            success = parse(x)
            return True
        except:
            pass
    return False

def GetNextLine(line,spl):
    try:
        return spl[spl.index(line) + 1]
    except:
        return ""

def CreateSlides(path,slides):
    f = open(path,"r",encoding='utf-8', errors='ignore')
    lines = f.readlines()
    slide_text = ""
    for line in lines:
        line = line.replace('²',"-")
        line = line.replace("\t"," bslash ")
        line = line.replace("§","\t")
        if "Chapter" in line:
            slides.append(slide_text)
            slide_text = ""
        if not ContainsDate(line) and line.count("/") < 2:
            line = line.replace("/"," slash ")
            slide_text += line
    for s in slides:
        spl = s.split("\n")
        title = spl[0]
        title = title.replace("","")
        if title == "":
            title = GetNextLine(title,spl)
            if title == "":
                continue
        text = "\n".join(spl[1:])
        dest = os.path.join(folder,title)
        while os.path.exists(dest):
            dest += "1"
        dest += ".txt"
        try:
            with open(dest,"w") as f:
                f.write(text)
        except:
            print()
            print(dest)
            print(text)
            print()
            #return dest

for path in paths:
    dest = CreateSlides(path,slides)
