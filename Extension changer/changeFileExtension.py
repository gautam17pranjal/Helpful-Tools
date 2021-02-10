# changing file extension from .vtt to .srt

import os, sys

folder = "Extension changer/test/"
files = os.listdir(folder)
for file in files:
    oldname = os.path.join(folder, file)
    if not os.path.isfile(oldname):
        continue
    newname = oldname.replace('.vtt', '.srt')
    output = os.rename(oldname, newname)
print("done")