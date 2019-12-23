import pytest
from varname import varname

def test_function():

	def function():
		return varname()

	func = function()
	assert func == 'func'

	func = function(
	)
	assert func == 'func'

	func = \
		function()
	assert func == 'func'

	func = function\
		()
	assert func == 'var_0'

	func = [function()]
	assert func == ['var_1']

def test_function_debug(caplog):
	def function():
		return varname(debug = True)
	func = function()
	assert '- Handing case:' in caplog.text
	assert '(where varname() was called)' in caplog.text
	assert 'Desired function/class was called in:' in caplog.text
	assert 'Looking for where exactly' in caplog.text
	assert 'Found at' in caplog.text

def test_function_context():

	def function(*args):
		return varname(context = 3)

	func = function(
		1, # I
		2, # have
		3, # a
		4, # long
		5, # argument
		6, # list
	)
	assert func == 'var_2'

	def function(*args):
		return varname(context = 20)

	func = function(
		1, # I
		2, # have
		3, # a
		4, # long
		5, # argument
		6, # list
	)
	assert func == 'func'

def test_function_deep():

	def function():
		# I know that at which stack this will be called
		return varname(caller = 3)

	def function1():
		return function()

	def function2():
		return function1()

	func = function2()
	assert func == 'func'

def test_class():

	class Klass:
		def __init__(self):
			self.id = varname()
		def copy(self):
			return varname()

	k = Klass()
	assert k.id == 'k'

	k2 = k.copy()
	assert k2 == 'k2'

def test_class_deep():

	class Klass:
		def __init__(self):
			self.id = self.some_internal()

		def some_internal(self):
			return varname(caller = 2)

		def copy(self):
			return self.copy_id()

		def copy_id(self):
			return self.copy_id_internal()

		def copy_id_internal(self):
			return varname(caller = 3)

	k = Klass()
	assert k.id == 'k'

	k2 = k.copy()
	assert k2 == 'k2'

def test_two_in_one():

	def func(*args):
		return varname()

	def func2():
		fun1 = func(
			1,
			2,
			3,
			4
		)
		fun2 = func(
			1,
			2,
			3,
			4,
			5
		)
		return fun1, fun2

	assert func2() == ('fun1', 'fun2')
