import json

from datetime import datetime


def today_is() -> str:
    """Very simple function that get date and time of the script 
    exection and return them in a formatted string.

    Returns:
        str: An underscore separeted string that contains date and time.

    Example:
        >>> from tools.helpers import today_is      
        >>> today = today_is()
        >>> print(today)
        1991_8_5_19h30min00s
    """
    today = datetime.now()
    date = f'{today.year}_{today.month}_{today.day}'
    time = f'{today.hour}h{today.minute}min{today.second}s'
    return f'{date}_{time}'


def log_lists_to_file(username: str, dict_to_log: dict) -> str:
    """Very simple function writes a given dict into a JSON file.

    Args:
        username (str): Instagram username.
        dict_to_log: The dict that is going to be written.

    Return:
        str: A message that confirms the creation of the file.

    Exemple:
        >>> from tools.helpers import log_lists_to_file
        >>> example = { 'hello' : 'world' }
        >>> msg = log_lists_to_file(username='brucewayne', dict_to_log=example)
        >>> print(msg)
        brucewayne_1991_8_5_19h30min00s.json Log File Created
    """
    today = today_is()
    filename = f'{username}_{today}.json'
    file = open(filename, 'w+')
    file.write(json.dumps(dict_to_log, indent=2))
    file.close()
    return f'{filename} Log File Created'
