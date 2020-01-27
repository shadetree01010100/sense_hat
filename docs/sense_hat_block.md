SenseHat
=======
Interact with the official RaspberryPi SenseHAT.

Properties
----------
- **IMU Sensor**: Contains three sensors, each with an `x`, `y`, and `z` axis, providing a combined 9 degrees of freedom when all are enabled.
  - *Accelerometer*: enable the accelerometer.
  - *Compass*: enable the compass.
  - *Gyroscope*: enable the gyroscope.

Example
-------
A dictionary of `key: value` pairs is added to each incoming signal for each enabled sensor.
```
{
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
