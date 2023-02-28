from unicodedata import name
from bebop_log_manager import BebopLoggingManager

from pyparrot.Bebop import Bebop

if __name__ == "__main__":
    logger = BebopLoggingManager()
    data = logger.get_all_data("ft_data_10_18_2022__0004.txt")
    print(type(data['MagnetoCalibrationStateChanged_calibrationFailed']))
    print([float(d) for d in data['MagnetoCalibrationStateChanged_calibrationFailed']])

    # bebop = Bebop(drone_type="Bebop2")

    # print("connecting")
    # success = bebop.connect(10)
    # print(success)

    # if (success):
    #     logger.init_logging_all()
    #     bebop.set_user_sensor_callback(logger.logging_callback, bebop.sensors.sensors_dict)

    #     print("sleeping")
    #     bebop.smart_sleep(2)

    #     bebop.safe_takeoff(10)

    #     bebop.smart_sleep(1)

    #     bebop.safe_land(10)

    #     print("DONE - disconnecting")
    #     bebop.disconnect()
    #     logger.end_logging()
