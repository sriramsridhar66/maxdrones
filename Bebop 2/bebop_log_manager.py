from datetime import datetime
from logger import Logger
from log_reader_writer import LogReaderWriter

class BebopLoggingManager:
    def __init__(self) -> None:
        self.logger = None
        self.log_editor = LogReaderWriter()
        self.start_time = self.get_timestamp()
        self.file_name = "ft_data_" + self.start_time + '.txt'
        return

    def init_logging_all(self):
        self.logger = Logger()
        pass

    def init_logging_specific(self, var_names: list = None):
        self.logger = Logger()
        print('LOGGING SPECIFIC VARS NOT A THING YET XD')
        pass

    def logging_callback(self, sensor_data):
        if self.logger is None:
            return
        self.logger.log_data(sensor_data)
        return

    def get_timestamp(self):
        now = datetime.now()
        date_time = now.strftime("%m_%d_%Y__%H%M")
        return date_time

    def end_logging(self, filename: str =None) -> None:
        if filename is not None:
            self.file_name = filename
        self.log_editor.write_to_file(self.logger.get_flight_data(), self.file_name)
        return

    def get_all_data(self, filename: str) -> dict:
        return self.log_editor.read_from_file(filename)