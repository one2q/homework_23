import os

from constants import DATA_DIR


def is_file_in_folder(file_name: str) -> bool:
	return file_name in os.listdir(DATA_DIR)


# filename = 'apache_logs.txt'


def generator_from_file(file_name: str):
	"""
	Make generator from file_name.txt
	"""
	with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as file:
		for line in file:
			yield line#.split(' ')


def filter_file(generator: generator_from_file, query: str) -> list[str]:
	result = list(filter(lambda x: query in x, generator))
	return result


def map_func(generator: generator_from_file, query: int) -> list[str]:
	result = list(map(lambda x:  x.split(' ')[int(query)], generator))
	return result


def unique(generator: generator_from_file, mock: any) -> list[str]:
	pre_result = set(generator)
	return list(pre_result)


def sort_func(generator: generator_from_file, query: str) -> list[str]:
	if query == 'desc':
		reverse = False
	else:
		reverse = True
	return sorted(generator, reverse=reverse)


def limit_func(the_list: list[str], amount: int) -> list[str]:
	return the_list[:int(amount)]


my_func = {
	'filter': filter_file,
	'map': map_func,
	'limit': limit_func,
	'sort': sort_func,
	'unique': unique,
}
