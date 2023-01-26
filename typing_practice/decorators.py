from dataclasses import dataclass, asdict

import marshmallow


class Person:
	def __init__(self, first_name: str, last_name: str, age: int):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age


@ dataclass
class Person:
	first_name: str
	last_name: str = "unknown"
	age: int = 15


p = Person("Vitaliy", "Stepanov", 34)
# print("p = ", p)
# print(asdict(p))


p1 = Person("Vitaliy", "Stepanov", 34)
p2 = Person("Anton")
# print("p1 = ", p1)
# print("p2 = ", p2)
# print("p==p1 - ", p == p1)
# print("p1==p2 - ", p1 == p2)




# ----------------------------------------------------------------
#	ФАБРИКИ СТАНДАРТНЫХ ЗНАЧЕНИЙ. ВСЁ ЛИ ХОРОШО С КОДОМ?
from dataclasses import field


@dataclass
class Adult(Person):
	children: list = field(default_factory=list)


ad = Adult("Ivan", "Ivanov")
# print(ad)



# ----------------------------------------------------------------
# Код ниже получает все типы лицензий с гитхаб

# from typing import List
#
# import requests
#
#
# def fetch_repos(org: str) -> dict:
# 	resp = requests.get(f"https://api.github.com/orgs/{org}/repos")
# 	return resp.json()
#
#
# def fetch_licenses(language) -> List[str]:
# 	repos = fetch_repos(language)
# 	res = set()
# 	for item in repos:
# 		license_dict = item["license"]
# 		topics = item["topics"]
# 		if license_dict:
# 			if language in topics:
# 				res.add(license_dict["key"])
# 	return print(list(res))
#
#
# fetch_licenses("python")


# ----------------------------------------------------------------
# Этот же код, используя dataclass

# from typing import List, Optional
#
# import requests
#
#
# def fetch_repos(org: str) -> dict:
# 	resp = requests.get(f"https://api.github.com/orgs/{org}/repos")
# 	return resp.json()
#
#
# @dataclass
# class License:
# 	key: str
# 	name: str
#
#
# @dataclass
# class Repo:
# 	id: int
# 	name: str
# 	full_name: str
# 	license: Optional[License]
# 	topics: list[]
#
#
# def fetch_licenses(language) -> List[str]:
# 	repos = fetch_repos(language)
# 	res = set()
# 	for item in repos:
# 		if item["license"]:
# 			license_obj = License(
# 				key = item["license"]["key"],
# 				name = item["license"]["name"]
# 			)
# 		else:
# 			license_obj = None
#
# 		repo = Repo(
# 			id=item["id"],
# 			name=item["name"],
# 			full_name=item["full_name"],
# 			license=license_obj,
# 			topics=item["topics"]
# 		)
# 		if repo.license:
# 			if language in repo.topics:
# 				res.add(repo.license.key)
# 	return print(list(res))


# ----------------------------------------------------------------
# Используя marshmallow dataclass (pip install marshmallow_dataclass)

# import marshmallow_dataclass
#
# @dataclass
# class Person:
# 	name: str
# 	age: float
#
# 	class Meta:
# 		unknown = marshmallow.EXCLUDE
#
#
# PersonSchema = marshmallow_dataclass.class_schema(Person)

# Person(**{"name": "alex", "age": 20, "ds": 123}) # Падает с ошибкой изза наличия неизвестного поля ds

# p5 = Person(**{"name": "alex", "age": "20"})
# print(type(p5.age))

# p10 = PersonSchema().load({"name": "alex", "age": "20", "ds": 123})
# print(p10)
# print(type(p10.age))



# ----------------------------------------------------------------
# Этот же код, используя dataclass и marshmallow_dataclass

from typing import List, Optional

import marshmallow_dataclass
import requests


def fetch_repos(org: str) -> dict:
	resp = requests.get(f"https://api.github.com/orgs/{org}/repos")
	return resp.json()


@dataclass
class License:
	key: str
	name: str

	class Meta:
		unknown = marshmallow.EXCLUDE

@dataclass
class Repo:
	id: int
	name: str
	full_name: str
	license: Optional[License]
	topics: List[str]

	class Meta:
		unknown = marshmallow.EXCLUDE


RepoSchema = marshmallow_dataclass.class_schema(Repo)


def fetch_licenses(language) -> List[str]:
	repos = fetch_repos(language)
	res = set()
	for item in repos:
		repo = RepoSchema().load(item)
		# print(repo)
		# break
		if repo.license:
			if language in repo.topics:
				res.add(repo.license.key)
	return list(res)


print(fetch_licenses("python"))
