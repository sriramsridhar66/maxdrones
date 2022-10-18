class BebopLoggingManager:
    def __init__(self) -> None:
        self.file_name = None
        pass

    def init_logging_all(self):
        pass

    def init_logging_specific(self, var_names: list = None):
        pass

    def get_timestamp(self):
        pass

    def end_logging(self, filename: str =None):
        self.file_name = filename
        pass