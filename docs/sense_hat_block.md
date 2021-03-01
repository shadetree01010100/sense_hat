SenseHat
=======
Interact with the official RaspberryPi SenseHAT.

Properties
----------
- **Environmental Sensors**:
  - *Barometric Pressure*: read the on-board pressure, in millibar.
  - *Temperature*: read the on-board temperature, in degrees Celsius.
  - *Relative Humidity*: read the on-board relative-humidity, in percent.
- **IMU Sensor**: Contains three sensors, each with an `x`, `y`, and `z` axis, providing a combined 9 degrees of freedom when all are enabled.
  - *Accelerometer*: enable the accelerometer.
  - *Compass*: enable the compass.
  - *Gyroscope*: enable the gyroscope.

Example
-------
Incoming signals are enriched with each of the selected environmental sensors. For each enabled sensor of the IMU a dictionary of `x`, `y`, and `z` axes is added.

```
{
  'pressure_mbar': 1000.1,
  'temperature_C': 22.2,
  'relative_humidity': 42.0,
  'accelerometer': {
      'x': 1.0,
      'y': 0.0,
      'z': 0.0,
  },
  'compass': {
      'x': 0.0,
      'y': 1.0,
      'z': 0.0,
  },
  'gyroscope': {
      'x': 0.0,
      'y': 0.0,
      'z': 1.0,
  },
}
```

Commands
--------
None
