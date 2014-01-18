Picnic.py
==========

Picnic.py helps you write python packages: ::
    
    picnic.py new PackageName

This creates a directory with all the files you need to get started: ::
    
    /PackageName_project
        /PackageName
            /setup.py
            /README.rst
            /packagename
                /__init__.py
                /packagename.py

Not enough ? Try this: ::

    picnic.py new MyPackage --author=Zulko --sphinx --gitinit --dev

Now you have a new package with a Sphinx documentation and a git repository for your project. And your package has been installed on your computer in *develop* mode (meaning you can change the code directly from this folder, without needing to reinstall the project).

These commands **also work on already-written packages**. For instance if I go in the ``setup.py``  folder and type ::
    
    picnic.py --remote=https://github.com/Zulko/MyPackage.git --ghpages


This will link my project to an existing Github repository and initialize the Github Pages for this project. Now I just need to push these on Github (see Cookbook below), which will give me `this repo <https://github.com/Zulko/MyPackage>`_ for the code, and `this page <http://zulko.github.io/MyPackage>`_ for the online documentation (you can change the look afterwards).



Installation and customization
--------------------------------

Picnic.py requires the awesome docopt_ package, that you can install with the classic ::

    pip install docopt 

To install Picnic.py, get a zip of the code, for instance on Github_, and unzip it in some folder. You can have a look at the file templates ``README.rst``, ``setup.py`` etc in subfolder ``picnic/files``, and customize them as you like.

Then, in the folder of the ``setup.py``, type ::

    sudo python setup.py install

or even better, use this command instead, it will enable you to change the templates even after the installation: :: 

    sudo python setup.py develop

And you are done ! Note that you can also install ``picnic.py`` with ``pip`` but it is not recommended as it doesn't allow you to change the templates.


Contribute !
------------

Picnic.py is an open source software originally written by Zulko_ and released under the MIT licence. Please help make picnic better, for instance by expanding the capabilities, providing advice for sounder standards if you are an experienced module-maker, reporting bugs, etc. We love forks and pull resquests !

And speaking about branches, there is `another one <https://github.com/jcsaaddupuy/picnic.py/tree/dev>`_ being actively developed.

Picnic is being developped on Github_. That's where you should go for troubleshooting and bug reports.




Cookbook  
---------

In this section, which is meant for beginners in Python, Sphinx, git, and Github, we explain how the files created by Picnic.py are meant to be used. You can also get help from the console with ::

    picnic.py --help


Creating a Python package
''''''''''''''''''''''''''''

To start a new project, you type ::

    picnic.py new PackageName

To install the package (you will be able to modify the code afterwards) type ::
    
    python setup.py develop

or equivalently ::
    
    picnic.py --dev
    
Now we can start to code: we go in directory ``PackageName/packagename`` and in the file ``packagename.py`` we write ::

    def say_hello():
        print "Hello world !"
    
To check that this worked, open a python console (in any folder) and type ::
    
    >>> import packagename
    >>> packagename.say_hello()
     Hello World !



Creating a Sphinx documentation
'''''''''''''''''''''''''''''''''

To initialize the Sphinx_ documentation you type ::
    
    picnic.py [new PackageName] --author="Your Name" --sphinx

The documentation source will be in the ``docs`` directory and the built (html) doc will be in the folder ``built_docs/html/``. To preview the docs after you have made some changes you can go into the ``docs`` repository and type ::

    make html
    firefox ../../built_docs/html/index.html

For convenience these two lines are already written in the ``docs/make_html.sh`` file, therefore you only need to type ::
    
    ./make_html.sh


Creating a git repository
''''''''''''''''''''''''''''''''''

To create a git repository the classic way, you generally add a  ``.gitignore`` file to your folder (to specify what kind of files not to include in the repo) and type these lines ::
    
    git init
    git add .
    git commit -m "Initial commit"
    
The ``--git`` option does exactly all this: it adds a .gitignore file to the folder and runs all these commands. Be sure to run it in the directory where your ``setup.py`` is.

Linking to a repository on Github
''''''''''''''''''''''''''''''''''


To put this git repository on a Github, first create a repo on Github (say no when they ask you whether to include a README file). Github should give you the url of the repo, something like ``https://github.com/Zulko/MyPackage.git``. Then in a console type ::

    git add remote origin https://github.com/Zulko/MyPackage.git

or equivalently ::

    picnic.py --remote=https://github.com/Zulko/MyPackage.git

To commit the changes to the git repo I generally do ::
    
    git commit -a -m "my description of the commit"
    
And after this, to push the changes on the online Github repo:

    git push origin master


Creating Github-pages
'''''''''''''''''''''''

Here we suppose that you have already linked your project to Github with ::

    git add remote origin https://link/to/your/repo.git
    
or equivalently ::

    picnic.py --remote=https://link/to/your/repo.git

Now all you have to do is ::
    
    picnic.py --ghpages

This creates a special git repository for the Github Pages in the directory ``built_docs/html``, which is the output directory of the documentation.

When you are happy with the way your documentation looks you go into folder ``built_docs/html`` and type ::

    git commit -a -m "my description of the commit"
    git push origin gh-pages

That's all there is to know !


.. _Zulko : https://github.com/Zulko
.. _Github : https://github.com/Zulko/picnic.py
.. _Sphinx : http://sphinx-doc.org/
.. _docopt: http://docopt.org/
