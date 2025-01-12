import json


def deserialize_json(file):
    with open(file, "r") as read_file:
        dict_list = json.load(read_file)
        return dict_list


def serialize_json(file, dict_list):
    with open(file, "w") as write_file:
        string = json.dumps(dict_list)
        write_file.write(string)


def format_array_to_dict(values_array):
    result = {}
    for value in values_array:
        result[value['id']] = value['value']
    return result


def generate_new_dict(tests_dict, values_dict):
    for test in tests_dict:
        if 'value' in test:
            test['value'] = values_dict[test['id']]
        if 'values' in test:
            generate_new_dict(test['values'], values_dict)


try:
    tests_file = input("Введите имя файла tests.json: ")
    values_file = input("Введите имя файла values.json: ")
    report_file = input("Введите имя файла report.json: ")

    tests = deserialize_json(tests_file)
    values = deserialize_json(values_file)

    format_values = format_array_to_dict(values['values'])
    generate_new_dict(tests['tests'], format_values)
    serialize_json(report_file, tests)
except (FileNotFoundError, KeyError):
    print("Файл с данным именем не найден")