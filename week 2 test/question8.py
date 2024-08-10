# Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
# 1. if file does not exists in source, print "no file found in source".
# 2. if same file already exists in target, print "file with same name already exists"


import shutil
try:
    shutil.copyfile('source/text.txt',"destination/text1.txt")
except FileNotFoundError:
    print("File is not found found in source")
except :
    print("File already exists ")