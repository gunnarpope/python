# Importing Packages

* Import all the functions in `myfunks` as f:

	>>> import mypkg.myfunks as f
	>>> f.print_a()
	a


* Import the whole package, and init it with the `__init__.py` file:

	>>> import mypkg
	Invoking __init__.py for mypkg
	>>> mypkg.A
	['quux', 'corge', 'grault']


* Another import method
	>>> from mypkg import myfunks as f
	>>> f.print_a()
	a
	
