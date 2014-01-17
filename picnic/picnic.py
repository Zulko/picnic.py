#! /usr/bin/env python

"""
Picnic.py, easy Package creation with python.

Usage:
  picnic.py [new <name>] [options]
  
Options:
  --author=<name>        Your name.
  --licence =<name>      MIT, LGPL
  --dev                  Runs: sudo python setup.py develop
  --sphinx               Initializes the sphinx documentation
  --gitinit              Runs: git init; git add . ; git commit -m "1st"
  --remote=<repo_url>    Runs:  git remote add origin <repo_url>
  --ghpages              Configures github-pages
  --help -h              Show this screen.
  
"""

import shutil
import os
import time
import subprocess as sp


module_path = os.path.dirname(os.path.realpath(__file__))
files_path = os.path.join(module_path, 'files')

def execute(*commands):
    for comm in commands:
        print ("picnic - Running : %s"%comm)
        p = sp.Popen(comm, shell=True, stderr = sp.PIPE)
        p.wait()
        print (p.stderr.read())
        

def copy_file(name,dst = None, replace=None):
    """
    Copy a file in the files/ subfolder at the given destination
    (see usage below) and change some stuff in the file
    
    name: file or path to file. The file copied will be files/name
    dst: name of the destination file (relative to working dir)
    changes: a dict of what to replace in the file, e.g.
        { '$PACKAGE_NAME':'MyCoolPackage', '$AUTHOR':'John Wayne'} 
    """
    if isinstance(name,list):
        name = os.path.join(*name)
    if isinstance(dst,list):
        dst = os.path.join(*dst)
    if dst is None:
        dst = name
    shutil.copyfile(os.path.join(files_path,name),dst)
    if replace:
        # replace what has to be replaced in the file template
        with open(dst, 'r') as f:
            s = f.read()
        for k,v in replace.items():
            s = s.replace(k,v)
        with open(dst, 'w') as f:
            s = f.write(s)


if __name__ == "__main__":    
    
    from docopt import docopt
    
    argv = docopt(__doc__)
    #print argv # for debugging
    
    
    name = os.path.basename(os.getcwd())
    infos = { "$YEAR": str(time.localtime().tm_year),
              "$PACKAGE_NAME":name,
              "$package_name":name.lower()}
    
    
    
    if argv['--author']:
        
        infos['$AUTHOR'] = argv['--author']
    
    # COMMANDS
    
    
    
    if argv["new"]:
        """ Create a basic layout for a new Python package """
        
        name = argv['<name>']
        name_l = name.lower()
        infos.update({"$PACKAGE_NAME":name,
                      "$package_name":name_l })
        
        # basic layout
        
        # make folder Name_project/Name/ and move there
        project_dir = name+'_project' 
        os.mkdir(project_dir)
        os.chdir(project_dir)
        os.mkdir(name)
        os.chdir(name)
        

        # root repository (setup.py etc.)

        for f in [ "README.rst",
                   "MANIFEST.in" ,
                   "LICENCE.txt",
                   "setup.py",
                   "ez_setup.py"]:
            copy_file(f, replace=infos)

        # make the code folder (named like the package, in lower case)
        os.mkdir(name_l)
        copy_file(['code','package_name.py'],
                  [name_l,name_l +'.py'], replace = infos)
        copy_file(['code','__init__.py'],
                  [name_l,"__init__.py"], replace = infos)
    
    
    
    ### OPTIONS
    
    # keep the absolute path of the setup directory in memory
    setup_dir = os.getcwd()
    
    
    if argv["--licence"]:
        """ Copy the corresponding licence in a LICENCE.txt file """
        
        infos['$LICENCE'] = argv["--licence"]
        
        try:
            filename = argv["--licence"]+'.txt'
            copy_file(['licences',filename], 'LICENCE.txt')
        except IOError:
            print ("Sorry, licence file not found.")
    
    
    
    if argv['--sphinx']:
        """ Initialize a sphinx documentation in folder \docs, with
        output in folder ../built_docs """
        
        if not argv['--author']:
            
            print ("sphinx requires --author=<name>")
        
        else:
            
            os.mkdir('docs')
            os.chdir('docs')
            os.mkdir('_static')
            os.mkdir('_template')
            for f in [ "conf.py",
                       "index.rst" ,
                       "make.bat",
                       "Makefile",
                       "makehtml.sh"]:
                copy_file(['sphinx',f],f, replace=infos)
            execute('make html')
            os.chdir(setup_dir)
    
    
    
    if argv['--gitinit']:
        """ copy a .gitignore, initialize a git repository,
            make a first commit """
            
        copy_file('.gitignore')
        execute('git init',
                'git add .',
                'git commit -m "Initial commit"')
    
    
    if argv['--remote']:
        """ Link the local repo to some remote repo on Github """
        execute('git remote add origin %s'%argv['--remote'])
    
    
    if argv["--ghpages"]:
        """
        Lookup the url of the github repo in the local git repo, then
        clone this project and branch it in the directory
        ../built_docs/html, which is the output folder of the Sphinx
        documentation. Build the documentation, commit everything,
        push on Github.
        """
        
        # get the Github repo's url from the local git repository.
        # horrible hack ahead, please look away now !
        f = sp.Popen([ 'git', "remote", "-v"], stdout = sp.PIPE)
        github_url = f.stdout.read().split('\t')[1].split(' ')[0]
        
        
        # Look at the folder ../built_docs/html, it it exists destroy
        # it and rebuild it
        built_docs_dir = os.path.join('..','built_docs')
        if not os.path.exists(built_docs_dir):
            os.mkdir(buit_docs_dir)
        
        built_docs_html_dir = os.path.join(built_docs_dir,'html')
        if os.path.exists(built_docs_html_dir):
            shutil.rmtree(built_docs_html_dir)
        os.mkdir(built_docs_html_dir)
        os.chdir(built_docs_html_dir)
        built_docs_html_dir = os.getcwd()
        
        # Create an orphan branch of the project in ../built_docs/html
        execute('git clone %s %s'%(github_url, '.'),
                "git checkout --orphan gh-pages",
                "git rm -rf .")
        
        # Add a README (for the Github repo page)
        copy_file(['gh-pages','README.rst'], 'README.rst', infos)
        # Add a .nojekill file so that Github won't throw away the css
        copy_file(['gh-pages','.nojekyll'], '.nojekyll')
        
        try:
            # try to (re-)build the docs
            os.chdir(os.path.join(setup_dir,'docs'))
            execute('make html')
            os.chdir(built_docs_html_dir)
        except:
            print ("Picnic.py: Error - couldn't  build the docs.")
            os.chdir(built_docs_html_dir)
        
        # Make a first commit with everything
        execute("git add .",
                'git commit -a -m "First documentation commit"')
        
        os.chdir(setup_dir) # back to 'main' folder
    
    
    if argv['--dev'] :
        
        execute("sudo python setup.py develop")
