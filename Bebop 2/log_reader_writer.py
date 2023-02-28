import json

class LogReaderWriter:
    def __init__(self) -> None:
        pass

    def write_to_file(self, data: dict, filename: str):
        with open(filename, 'w') as to_write:
            to_write.write(json.dumps(data))

    def read_from_file(self, filename: str):
        data = None
        with open(filename) as to_read:
            data = json.load(to_read)
        return data