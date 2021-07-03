import os

from os import path

dir='./data/'
files = os.listdir(dir)
c = 0

def renameToValid(fro,to,dir,name):
    fpF = dir+name
    fpT = dir+name.replace(fro, to).replace('__','_').replace(' ','')
    print('From:',fpF)
    print('To:',fpT)
    if fpT is fpF or fpT == fpF:
        print('The filename are the same.')
        return
    if path.isfile(fpT):
        print('duplicated, delete.')
        os.remove(fpF)
        return
    os.rename(fpF,fpT)


for i, name in enumerate(files):

    fro = '_'
    to = '_'
    if fro in name:
        renameToValid(fro,to,dir,name)

    fro = '.jpeg_'
    to = '_'
    if fro in name:
        renameToValid(fro,to,dir,name)

    fro = '.jpg_'
    to = '_'
    if fro in name:
        renameToValid(fro,to,dir,name)