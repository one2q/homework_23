import json

from funcs import is_file_in_folder, my_func, generator_from_file

from flask import Flask, request

app = Flask(__name__)


@app.post("/perform_query")
def perform_query():
	user_request = request.json
	file_name = user_request.get('file_name')
	cmd1 = user_request.get('cmd1')
	value1 = user_request.get('value1')
	cmd2 = user_request.get('cmd2')
	value2 = user_request.get('value2')

	if None in (file_name, cmd1, value1, cmd2, value2):
		raise Exception('Проверьте правильность ввода команд и значений')

	if not is_file_in_folder(file_name):
		raise Exception("Нет такого файла в папке /data")

	data = generator_from_file(file_name)

	first = my_func.get(cmd1)
	second = my_func.get(cmd2)

	pre_result = first(data, value1)
	result = second(pre_result, value2)

	return app.response_class(
		json.dumps(
			result, ensure_ascii=True, indent=4
		), content_type="text/plain", status=200
	)


if __name__ == '__main__':
	app.run(port=8000)
