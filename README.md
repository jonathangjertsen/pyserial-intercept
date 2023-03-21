# pyserial-intercept

Intercept serial port traffic using pyserial and com0com

## How to use

First, get com0com https://sourceforge.net/projects/com0com/ and set up serial ports using the Ports class:

![port](https://user-images.githubusercontent.com/7355797/226605625-9c6cee36-2321-456b-a814-1c7443b01bed.PNG)

Configure the software you are snooping on to use one of the ports (here we will use COM23). Set the other one as `--port-pc` in the Python script.
Set the serial port for your DUT to `--port-dut`.

Example, where the serial port for the DUT is COM3:

```sh
python serial_intercept.py --port-dut=COM3 --port-pc=COM22
```

Data will be printed as it comes in, comma separated (time, device, data) so you can pipe the output to a CSV file.

```csv
1679401764.1944354,PC,0d
1679401764.1944354,DUT,90
1679401764.1964383,PC,3e380606040000000000c3c1
1679401764.1974308,DUT,90
1679401764.1984382,PC,3e32040400000000c5c9
1679401764.1994383,DUT,80001e1e00000000000001000105010347343330424f4f542c4d53502d47616e67004dcc
1679401764.7024062,PC,3e32040400000000c5c9
1679401764.7033985,DUT,80001e1e00000000000001000105010347343330424f4f542c4d53502d47616e67004dcc
1679401764.7044058,PC,3e410606000000000000c7b8
...
```
