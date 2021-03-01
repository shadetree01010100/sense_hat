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
Incoming signals are enriched with each of the selected environmental sensors. A dictionary of `key: value` pairs is added to each incoming signal for each enabled sensor of the IMU.

```
{
  'pressure_mbar': 1000,
  'temperature_C': 12.3,
  'relative_humidity': 42.0,
  '<accelerometer|compass|gyroscope>': {
      'x': <float>,
      'y': <float>,
      'z': <float>,
  }
}
```

Commands
--------
None
