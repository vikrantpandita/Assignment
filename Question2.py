import time
import os

timestr = time.strftime("%Y-%m-%d")
directory = timestr
  
parent_dir = "D:\coding"
  
path = os.path.join(parent_dir, directory)
if os.path.isdir(path):
    pass
else:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
os.chdir(path)
where = input('name of the file  ')


text = input('taking input from user ')


saveFile = open(where, 'w')
saveFile.write(text)
saveFile.close()