from typing import Dict, Callable

from functions import filter_query, unique_query, limit_query, map_query, sort_query

CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd, value, file_name, data):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    func = CMD_TO_FUNCTIONS[cmd]
    func_result = func(value=value, data=prepared_data)

    return list(func_result)
