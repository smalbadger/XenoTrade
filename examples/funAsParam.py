def foo(fun):
	print(fun())
	
def bar():
	return "This is bar yo"
	
def what():
	return "This is what yo"
	
def who():
	return
	
foo(bar)
foo(what)
foo(who)
foo(lambda: 5+21)
