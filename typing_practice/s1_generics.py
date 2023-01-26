from typing import List, Dict, Iterable


class Person:
	def __init__(self, name: str) -> None:
		self.name = name

	def get_greeting(self) -> str:
		buf = "Hello " + self.name
		return buf


def fetch_persons() -> List[Person]:
	return [Person("Vitaliy"), Person("Anton")]


def convert_dict_persons_to_list(persons: Dict[str, Person]) -> List[Person]:
	return list(persons.values())


def convert_dict_persons_to_list_2(persons: Dict[str, Person]) -> Iterable[Person]:
	return list(persons.values())


convert_dict_persons_to_list({"123": Person("1")})
convert_dict_persons_to_list({})
