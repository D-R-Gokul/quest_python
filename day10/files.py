import os
import shutil

os.makedirs("folder1")
file = open("folder1/text.txt", "x")
file.close()
os.makedirs("folder2")
shutil.copyfile('folder1/text.txt',"folder2/text1.txt")