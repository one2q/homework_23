from funcs import is_file_in_folder, filter_file, map_func


def test_is_file_in_folder():
	result = is_file_in_folder('test_file.txt')
	assert result == True, 'Что то не так с определением есть ли файл в папке'


def test_filter_func(generator):
	res = filter_file(generator, 'test')
	assert res == ['123 123 test'], 'Функция фильтра работает не корректно'


def test_map_func(generator):
	res = map_func(generator, 0)
	assert res == ['1', '2', '3', '123']

