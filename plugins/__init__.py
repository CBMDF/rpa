from abc import ABC


class Plugin(ABC):
    def __init__(self):
        print(f'Invoking __init__.py for {__name__}')
