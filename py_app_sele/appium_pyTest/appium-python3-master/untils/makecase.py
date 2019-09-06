""" 
@author: lileilei
@file: beijing.py 
@time: 2018/4/19 10:32 
"""
import  os
path=os.getcwd()
def  readheader():
    path_new=path+'//template//case.txt'
    return open(path_new,encoding='utf-8').read()
def readerconet():
    path_new = path + '//template//content.txt'
    conet = open(path_new, encoding='utf-8').read()
    return conet
def  makecasefile(casename,desc,funtionname):
    filepath=path+'//testcase//'+casename+'casetest.py'
    print(filepath)
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(readheader().format(casename, casename))
    with open(filepath, 'a', encoding='utf-8') as file:
        file.write(readerconet().format(funtionname, desc))