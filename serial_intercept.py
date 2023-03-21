from argparse import ArgumentParser

from serial import Serial

def main():
    parser = ArgumentParser()
    parser.add_argument("--port-dut")
    parser.add_argument("--port-pc")
    args = parser.parse_args()

    ser_dut = Serial(args.port_dut, timeout=0)
    ser_pc  = Serial(args.port_pc,     timeout=0)

    while True:
        data_pc = bytearray()
        while (x := ser_pc.read()):
            data_pc.extend(x)
        if data_pc:
            ser_dut.write(data_pc)
            print(f"PC,{''.join(format(x, '02x') for x in data_pc)}")

        data_dut = bytearray()
        while (x := ser_dut.read()):
            data_dut.extend(x)
        if data_dut:
            ser_dut.write(data_dut)
            print(f"DUT,{''.join(format(x, '02x') for x in data_dut)}")
            ser_pc.write(data_dut)

if __name__ == "__main__":
    main()
