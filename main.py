import serial
import socket
import time

s = serial.Serial("/dev/ttyACM0", baudrate=1000000)
socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
start_time = time.time_ns()
counter = 0
while True:
    counter += 1
    readed = s.readline()
    #print(readed)
    x = int(readed).to_bytes(4, byteorder="little")
    socket.sendto(x,("127.0.0.1",8080))
    elapsed_time = time.time_ns() - start_time
    if elapsed_time > 1000000000:
#        print("Frequency: {} Hz, ".format(counter))
        counter = 0
        start_time = time.time_ns()