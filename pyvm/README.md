# Python Virtual Environments
# notes from:
# https://docs.python.org/3/tutorial/venv.html

* Create a virtual environment for a project

	~/repos/python/pyvm $ python3 -m venv tutorial-env
	~/repos/python/pyvm $ ls
	README.md  tutorial-env

* Activate the virtual environment

	~/repos/python/pyvm $ source tutorial-env/bin/activate

* Install the requests package
	
	(tutorial-env) ~/repos/python/pyvm $ pip install requests==2.6.0
	Collecting requests==2.6.0
	  Downloading https://files.pythonhosted.org/packages/73/63/b0729be549494a3e31316437053bc4e0a8bb71a07a6ee6059434b8f1cd5f/requests-2.6.0-py2.py3-none-any.whl (469kB)
	    100% |████████████████████████████████| 471kB 996kB/s 
	Installing collected packages: requests
	Successfully installed requests-2.6.0

* List all of the installed packages in this repo

	(tutorial-env) ~/repos/python/pyvm $ pip list
	Package    Version
	---------- -------
	pip        18.1   
	requests   2.6.0  
	setuptools 40.6.2 

* Get a snapshot of the requirements

	(tutorial-env) ~/repos/python/pyvm $ pip freeze > requirements.txt
	(tutorial-env) ~/repos/python/pyvm $ cat requirements.txt 
	requests==2.6.0

* Other users can install the required packages using `install -r`


	(tutorial-env) ~/repos/python/pyvm $ pip install -r requirements.txt 




