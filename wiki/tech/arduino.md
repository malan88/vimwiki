# Arduino notes

## Calculating resistor values
The resistor value is calculated using the following formula:

(Operating voltage – LED forward voltage) / current in amperes = 
    resistor value in ohms

As a rule of thumb, most LEDs can take a maximum of 20 mA of current before
suffering damage; mA stands for milliamperes, usually called milliamps. Forward
operating voltage for red, yellow, and orange LEDs is 1.5V, for green LEDs 2.0V,
and for blue and white LEDs 3.0V.

You’re going to use the USB connection for power, which is 5V. If you’re using
red LEDs, which have a forward voltage value of 1.5V, and a current of 20 mA,
you can calculate the needed resistance as follows:

(5V – 1.5V) / 0.02 A = 175 ohms

The nearest available resistor is 180 ohms, so to safely protect the LED, you
need to use a resistor of 180 ohms or greater. We used 270 ohm resistors because
we had plenty of them available, and the LEDs still light up when using them.
