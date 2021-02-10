import os, sys

folder = "Extension changer/test/"
files = os.listdir(folder)
for file in files:
    infilename = os.path.join(folder, file)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(file)
    newname = infilename.replace('.vtt', '.srt')
    output = os.rename(infilename, newname)
print("done")