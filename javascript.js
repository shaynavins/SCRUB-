sensors.infrared2.onEvent(InfraredSensorEvent.ObjectDetected, function () {
    motors.largeD.run(37, -90, MoveUnit.Degrees)
    control.waitMicros(4000)
    motors.largeD.run(37, 90, MoveUnit.Degrees)
})
sensors.color1.onColorDetected(ColorSensorColor.Red, function () {
    motors.largeC.run(37, -90, MoveUnit.Degrees)
    control.waitMicros(3000)
    motors.largeC.run(37, 90, MoveUnit.Degrees)
})
