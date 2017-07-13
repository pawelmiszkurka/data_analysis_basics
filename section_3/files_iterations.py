import os
import glob

gzlist=glob.glob("*.gz")
print(gzlist)

for file in gzlist:
	filename=os.path.splitext(file)[0]
	newname=filename+"zip"
	os.rename(file,newname)