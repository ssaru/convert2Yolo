import logging



class Reader:
    def __init__(self):
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def _is_validated_file(self, filename: str) -> bool:
        raise NotImplementedError
