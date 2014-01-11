Picnic
=======

Picnic is a simple template engine for writing python modules. You open a console and in any folder you type ::
    
    picnic.py ModuleName

and it will produce the following folder, with (almost ?) all the files you need. All there is left to do is write the actual code : ::

    /ModuleName
        /modulename
            /__init__.py
            /modulename.py # A file for the actual code
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

The ``-git`` option will initialize a git repository will the newly created module (if ``git`` is installed): ::
    
    # it will run these lines in the ModuleName folder
    git init
    git add .
    git commit -m "Initial commit"
    # it will also create a python-specific .gitignore file

The ``-dev`` option will run the following command at the end to install the newly created module in *develop* mode (i.e. you can do your changes on the module without needing to reinstall the module each time to test it) ::
    
    sudo python setup.py develop

Installation and customization
--------------------------------

From the source
''''''''''''''''

Get a zip of the code, for instance on Github_ . Unzip the code in some folder. You can the models of the files ``README.rst``, ``setup.py`` etc in subfolder ``picnic/files`` and change them as you like.
Then use the following command in the folder where the ``setup.py`` is ::

    sudo python picnic.py install

Or even better, use this command instead, it will enable you to change the models of the files even after the installation: :: 

    sudo python picnic.py develop


With pip (not recommanded)
'''''''''''''''''''''''''''

Type this in a terminal ::

    sudo pip install picnic

The problem with this installation is that you cannot customize the templates.

Test
'''''

To test if it works go to any folder and type ::
    
    picnic.py TestModule



Contribute
-----------

Picnic is an open source software originally written by Zulko_ and released under the MIT licence. Please help make picnic better, for instance by expanding the capabilities, providing advice for sounder standards if you are an experienced module-maker, reporting bugs, etc. We love forks and pull resquests !
Picnic is being developped on Github_, that's where you should go for troubleshooting and bug reports.

.. _Zulko : https://github.com/Zulko
.. _Github :  https://github.com/Zulko/picnic.py
