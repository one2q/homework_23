import os
import re
from typing import Generator, Any

from constants import DATA_DIR


def is_file_in_folder(file_name: str) -> bool:
	return file_name in os.listdir(DATA_DIR)


# filename = 'apache_logs.txt'


def generator_from_file(file_name: str) -> Generator:
	"""
	Make generator from file_name.txt
	"""
	with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as file:
		for line in file:
			yield line


def filter_file(generator: Generator, query: str) -> list[str]:
	result = list(filter(lambda x: query in x, generator))
	return result


def map_func(generator: Generator, query: int) -> list[str]:
	result = list(map(lambda x:  x.split(' ')[int(query)], generator))
	return result


def unique(generator: Generator, mock: Any) -> list[str]:
	pre_result = set(generator)
	return list(pre_result)


def sort_func(generator: Generator, query: str) -> list[str]:
	if query == 'desc':
		reverse = True
	else:
		reverse = False
	return sorted(generator, reverse=reverse)


def limit_func(the_list: list[str], amount: int) -> list[str]:
	return the_list[:int(amount)]


def regex_func(generator: Generator, value: str) -> list[str]:
	r = re.compile(value)
	result = [i for i in generator if r.findall(i)]
	return result


#  TODO что то вместо object должно быть но пока не понятно что
my_func: dict[str, object] = {
	'filter': filter_file,
	'map': map_func,
	'limit': limit_func,
	'sort': sort_func,
	'unique': unique,
	'regex': regex_func,
}

