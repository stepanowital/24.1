def hello():
	var1: int = 0
	var2: str = "hello"
	var3: dict = {"hello"}


def greeting(name: str) -> str:
	return "Hello " + name


class Person:
	def __init__(self, name: str) -> None:
		self.name = name

	def get_greeting(self) -> str:
		buf = "Hello " + self.name
		return buf


res = greeting("Vitaliy")
print(res.upper())

p: Person = Person("Alex")
p1 = Person("John")
print(p.get_greeting().upper())
print(p1.get_greeting().upper())

p2 = Person(2)
print(p2.name)