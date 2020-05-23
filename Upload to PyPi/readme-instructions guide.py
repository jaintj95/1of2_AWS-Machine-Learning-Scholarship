'''

quick notes
1. you need to change the directory of you VE to where your package is located
2. Execute "python setup.py sdist"
3. ensure that the "package name" is correct and the same as the folder containing the package
- there could be errors up loading the same package with the same "verision"
4. if all is well, then two files will be created: dist and "package-name.egg-info"
5. execute "pip install twine"
6. execute "twine upload --repository-url https://test.pypi.org/legacy/ dist/*"
7. execute "pip install --index-url https://test.pypi.org/simple <package name>"

for the regular PyPi
8. execute "twine upload dist/*"

>>to uninstall--pip uninstall "package_name"

pip installing you use the "-" (dash)
else you use "_" (underscore)
youtube help
https://youtu.be/4uosDOKn5LI?t=486


-------------------------------

In this part of the lesson, you'll practice uploading a package to PyPi.

The Python package is located in the folder 5_exercise_upload_to_pypi

You'll need to create a setup.cfg file, README.md file, and license.txt file.
You'll also need to create accounts for the pypi test repository and pypi repository.

Don't forget to keep your passwords; you'll need to type them into the command line.

Once you have all the files set up correctly, you can use the following
commands on the command line (note that you need to make the name of the
package unique, so change the name of the package from distributions to
something else. That means changing the information in setup.py and the folder name):

cd 5_exercise_upload_to_pypi
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ distributions

# command to upload to the pypi repository
twine upload dist/*
pip install distributions

If you get stuck, rewatch the previous video showing how to upload a package to PyPi.
'''
