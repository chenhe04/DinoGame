import serial
import threading

class BlinkReader:
    def __init__(self, port="COM3", baudrate=9600):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.blink_detected = False
        self.running = True
        threading.Thread(target=self.read_loop, daemon=True).start()

    def read_loop(self):
        while self.running:
            line = self.ser.readline().decode().strip()
            if line == "BLINK":
                self.blink_detected = True

    def consume_blink(self):
        if self.blink_detected:
            self.blink_detected = False
            return True
        return False

    def close(self):
        self.running = False
        self.ser.close()
