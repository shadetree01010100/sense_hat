from sense_hat import SenseHat
from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import BoolProperty, ObjectProperty, PropertyHolder, \
    VersionProperty


class IMUsensor(PropertyHolder):
    accel = BoolProperty(title='Accelerometer', default=True, order=0)
    compass = BoolProperty(title='Compass', default=True, order=1)
    gyro = BoolProperty(title='Gyroscope', default=True, order=2)


class SenseHAT(Block, EnrichSignals):

    imu = ObjectProperty(IMUsensor, title='IMU Sensor')
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
        outgoing_signals = []
        for signal in signals:
            outgoing_signals.append(self.get_output_signal(data, signal))
        self.notify_signals(outgoing_signals)
