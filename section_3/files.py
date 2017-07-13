import os

fullpath="/Users/pmiszkurka/python/section_3/someFile.txt"
filename=os.path.basename(fullpath)

if not os.path.exists(fullpath):
	os.makedirs(fullpath)

os.path.splittext(fullpath)[0]