from unittest.mock import patch, Mock
from nio import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..sense_hat_block import SenseHAT


@patch(SenseHAT.__module__ + '.SenseHat')
class TestSenseHat(NIOBlockTestCase):

    maxDiff=None
    def test_accelerometer(self, mockSenseHat):
        """Signals are enriched with accelerometer data."""
        mock_hat = Mock()
        mock_hat.get_accelerometer_raw.return_value = {
            'x': -1,
            'y': 0,
            'z': 1,
        }
        mockSenseHat.return_value = mock_hat
        blk = SenseHAT()
        self.configure_block(blk, {
            'imu': {
                'accel': True,
                'compass': False,
                'gyro': False,
            },
            'enrich': {
                'exclude_existing': False,
            },
        })

        blk.start()
        mockSenseHat.assert_called_once_with()
        mock_hat.set_imu_config.assert_called_once_with(True, False, False)

        blk.process_signals([Signal({'pi': 3.14})])
        mock_hat.get_accelerometer_raw.assert_called_once_with()
        mock_hat.get_compass_raw.assert_not_called()
        mock_hat.get_gyroscope_raw.assert_not_called()

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assert_last_signal_list_notified([
            Signal({
                'accelerometer': {
                    'x': -1,
                    'y': 0,
                    'z': 1,
                },
                'pi': 3.14,
            }),
        ])

    def test_compass(self, mockSenseHat):
        """Signals are enriched with compass data."""
        mock_hat = Mock()
        mock_hat.get_compass_raw.return_value = {
            'x': -1,
            'y': 0,
            'z': 1,
        }
        mockSenseHat.return_value = mock_hat
        blk = SenseHAT()
        self.configure_block(blk, {
            'imu': {
                'accel': False,
                'compass': True,
                'gyro': False,
            },
            'enrich': {
                'exclude_existing': False,
            },
        })

        blk.start()
        mockSenseHat.assert_called_once_with()
        mock_hat.set_imu_config.assert_called_once_with(False, True, False)

        blk.process_signals([Signal({'pi': 3.14})])
        mock_hat.get_accelerometer_raw.assert_not_called()
        mock_hat.get_compass_raw.assert_called_once_with()
        mock_hat.get_gyroscope_raw.assert_not_called()

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assert_last_signal_list_notified([
            Signal({
                'compass': {
                    'x': -1,
                    'y': 0,
                    'z': 1,
                },
                'pi': 3.14,
            }),
        ])

    def test_gyroscope(self, mockSenseHat):
        """Signals are enriched with gyroscope data."""
        mock_hat = Mock()
        mock_hat.get_gyroscope_raw.return_value = {
            'x': -1,
            'y': 0,
            'z': 1,
        }
        mockSenseHat.return_value = mock_hat
        blk = SenseHAT()
        self.configure_block(blk, {
            'imu': {
                'accel': False,
                'compass': False,
                'gyro': True,
            },
            'enrich': {
                'exclude_existing': False,
            },
        })

        blk.start()
        mockSenseHat.assert_called_once_with()
        mock_hat.set_imu_config.assert_called_once_with(False, False, True)

        blk.process_signals([Signal({'pi': 3.14})])
        mock_hat.get_accelerometer_raw.assert_not_called()
        mock_hat.get_compass_raw.assert_not_called()
        mock_hat.get_gyroscope_raw.assert_called_once_with()

        blk.stop()
        self.assert_num_signals_notified(1)
        self.assert_last_signal_list_notified([
            Signal({
                'gyroscope': {
                    'x': -1,
                    'y': 0,
                    'z': 1,
                },
                'pi': 3.14,
            }),
        ])
