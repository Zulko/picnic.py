# This Picnic.py test example supposes that you have
# - installed Sphinx and git
# - created a repo on Github called MyPackage (change url below)
#
# It will create from scratch a new Package called MyPackage,
# initialize a Sphinx documentation and a git, install the package in
# develop mode, link the package to its Github repo, make the
# Github Pages and upload the package and its pages on Github

picnic.py new MyPackage --author=Zulko --sphinx --gitinit --dev

# Link to Github, initialize Github Pages
cd MyPackage_project/MyPackage
picnic.py --remote=https://github.com/Zulko/MyPackage.git --ghpages

# Push the Repository on Github
git push origin master

# Push the Github Pages on Github
cd ../built_docs/html
git push origin gh-pages
