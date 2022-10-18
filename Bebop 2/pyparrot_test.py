from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop2")

print("connecting")
success = bebop.connect(10)
print(success)

if (success):

    print("sleeping")
    bebop.smart_sleep(2)

    bebop.safe_takeoff(10)

    bebop.smart_sleep(2)

    bebop.safe_land(10)

    print("DONE - disconnecting")
    print(bebop.sensors.battery)
    bebop.disconnect()