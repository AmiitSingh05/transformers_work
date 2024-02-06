import csv
import json

# collecting the path of file from the configuration.json file
default_config_file_name = "configuration.json"
def get_second_item(csv_file_path):
    """
    csv file is containing 2 fields one in index second is name.
    This function collects the names
    :param csv_file_path: file path
    :return: list of names
    """
    second_items = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            # Check if the row has at least two items
            if len(row) >= 2:
                second_item = row[1]
                second_items.append(second_item)

    return second_items


def get_name_list():
    """
    This function collect the file path from configuration file and
    calls get_second_item to get list of name
    :return: list of name
    """
    with open(default_config_file_name, 'r') as fd:
        fd_open = json.load(fd)
        csv_file_path = fd_open['csv_file_path']
    return get_second_item(csv_file_path)


