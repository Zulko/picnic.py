Picnic - Let's sit there !
==========================

Picnic is a simple template engine for writing python modules. In a console you type ::
    
    picnic.py ModuleName

and it will produce the following folder, with (almost ?) everything you need to start worrying about the actual code: ::

    /ModuleName
        /modulename
            /__init__.py
            /modulename.py
        /setup.py
        /README.rst
        /LICENCE.txt
        /MANIFEST.in 
        /ez_setup.py # for Setuptools  

The created package is configured to work with Setuptools because Setuptools rocks.

Options
--------

Two useful options are ``-git`` and ``-dev`` (the order doesn't matter): ::
    
    picnic.py ModuleName -git -dev

The option ``-git`` will initialize a git repository will the newly created module (if ``git`` is installed): ::
    
    # it will run these lines in the ModuleName folder
    git init
    git add .
    git commit -m "Initial commit"
    # it will also create a python-specific .gitignore file

The option ``-dev`` will run the following command at the end to install the newly created module in *develop* mode (i.e. you can do your changes on the module without needing to reinstall the module each time to test it) ::
    
    sudo python setup.py develop

Installation and customization
--------------------------------

Picnic gets installed as usual: either with pip with a command like ::

    sudo pip install picnic

Or you can unzip the code in some folder. Then you can check the files models (in subfolder picnic/files) and change them as you like. Then use the following command in the folder where the ``setup.py`` is ::

    sudo python picnic.py install

Or even better, you can use this command, which will enable you to change the models of the files even after the installation: :: 

    sudo python picnic.py develop


