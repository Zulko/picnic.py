#! /usr/bin/env python

import shutil
import os

module_path = os.path.dirname(os.path.realpath(__file__))
files_path = os.path.join(module_path, 'files')

def new_file(filename, content=''):
    """ Creates a new file and initializes it with the given content."""
    with open(filename, 'a') as f:
        f.write(content)

def copy_file(name,dst = None):
    """ copy a file in the files/ subfolder at the given destination
    (see usage below) """
    if dst is None:
        dst = name
    shutil.copyfile(os.path.join(files_path,name),dst)

def change_file(filename, dic):
    """ replaces words by other words in the file. dic must be a
    dictionnary like {'word1': 'replacement1', 'word2': ... etc.} """ 
    with open(filename, 'r') as f:
        s = f.read()
    for k,v in dic.items():
        s = s.replace(k,v)
    with open(filename, 'w') as f:
        s = f.write(s)
        

if __name__ == "__main__":

    import sys

    name = sys.argv[1]

    # BASIC LAYOUT

    os.mkdir(name)
    os.chdir(name)

    # root repository (setup.py etc.)

    for f in [ "README.rst",
               "MANIFEST.in" ,
               "LICENCE.txt",
               "setup.py",
               "ez_setup.py"]:
        copy_file(f)
        change_file(f,{"$PACKAGE_NAME":name})

    # code repository

    namel = name.lower()
    os.mkdir(namel)
    new_file(os.path.join(namel,namel +'.py'), '""" %s """'%name)
    init = os.path.join(namel,"__init__.py")
    copy_file('__init__.py', init)
    change_file(init,{"$PACKAGE_NAME":name})
    
    
    # OPTIONS

    if '-doc' in sys.argv:
        os.mkdir('docs')

    if '-git' in sys.argv:
        copy_file('.gitignore')
        os.system('git init ; git add . ;')
        os.system('git commit -m "Initial commit"')

    if '-dev' in sys.argv:
        os.system("sudo python setup.py develop")
