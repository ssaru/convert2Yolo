import logging
import json


class Parser:

    ALLOW_EXTENSION = 'json'

    def __init__(self, proto_path: str):
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)
        self.proto: dict = self._load_proto(proto_path)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def _load_proto(self, proto_file_path: str):
        self._is_json(proto_file_path)
        with open(proto_file_path) as f:
            proto = json.load(f)

        return proto

    def _is_json(self, path: str) -> None:
        extension: str = path.split(".")[-1].lower()
        if extension != "json":
            self.logger.debug("Debug: proto file is not json")
            raise RuntimeError("file is not json")

if __name__ == "__main__":
    proto_path = "../config/proto.json"
    parser = Parser(proto_path)
    _proto = parser.proto
    print(_proto)
    print(type(_proto))
    print(_proto.keys())
