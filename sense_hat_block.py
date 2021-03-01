from sense_hat import SenseHat
from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import BoolProperty, ObjectProperty, PropertyHolder, \
    VersionProperty


class EnvironmentalSensors(PropertyHolder):
    press = BoolProperty(title='Barometric Pressure', default=True, order=0)
    rh = BoolProperty(title='Relative Humidity', default=True, order=1)
    temp = BoolProperty(title='Temperature', default=True, order=2)


class IMUsensor(PropertyHolder):
    accel = BoolProperty(title='Accelerometer', default=True, order=0)
    compass = BoolProperty(title='Compass', default=True, order=1)
    gyro = BoolProperty(title='Gyroscope', default=True, order=2)


class SenseHAT(Block, EnrichSignals):

    env = ObjectProperty(
        EnvironmentalSensors,
        title='Environmental Sensors',
        order=0)
    imu = ObjectProperty(IMUsensor, title='IMU Sensor', order=1)
    version = VersionProperty('0.1.0')

    def __init__(self):
        super().__init__()
        self.hat = None

    def configure(self, context):
        super().configure(context)
        self.hat = SenseHat()
        self.hat.set_imu_config(
            self.imu().accel(),
            self.imu().compass(),
            self.imu().gyro())

    def process_signals(self, signals):
        data = {}
        if self.imu().accel():
            data['accelerometer'] = self.hat.get_accelerometer_raw()
        if self.imu().compass():
            data['compass'] = self.hat.get_compass_raw()
        if self.imu().gyro():
            data['gyroscope'] = self.hat.get_gyroscope_raw()
        if self.env().rh():
            data['relative_humidity'] = self.hat.get_humidity() * 100
        if self.env().temp():
            data['temperature_C'] = self.hat.get_temperature()
        if self.env().press():
            data['pressure_mbar'] = self.hat.get_pressure()
        outgoing_signals = []
        for signal in signals:
            outgoing_signals.append(self.get_output_signal(data, signal))
        self.notify_signals(outgoing_signals)
