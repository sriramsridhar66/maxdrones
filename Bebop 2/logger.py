class Logger:
    def __init__(self) -> None:
        self.sensor_dict = {}
        return

    def log_data(self, sensor_data:dict) -> None:
        for key, val in sensor_data.items():
            if key in self.sensor_dict:
                self.sensor_dict[key].append(str(val))
            else:
                self.sensor_dict[key] = [str(val)]

    def get_flight_data(self) -> dict:
        return self.sensor_dict