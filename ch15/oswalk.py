
import os


listfiles = os.walk("d:/工作文档/日常工作")

for dirpath,dirname,filename in listfiles:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------')
