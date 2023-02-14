'''
Module Main
'''

import json

from traceback import format_exc
from instagram.instagram import Instagram


def main() -> None:
    '''
    Function main
    '''
    bbb = Instagram(
        user='',
        password='')

    bbb.get_paths()
    bbb.get_instagram()
    bbb.extract()
    print(json.dumps(obj=bbb.list_of_users))


if __name__ == '__main__':
    try:
        main()

    except Exception:
        ERROR = format_exc().replace('\n', ' ')
        print(ERROR)
