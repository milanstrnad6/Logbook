#!/usr/bin/python
# Filename: text.py
import serial
import time
import POINTS

def start():
        ser = serial.Serial("/dev/ttyS0",115200)

        W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n","AT+CGNSTST=1\r\n"]
        ser.write(W_buff[0])
        ser.flushInput()
        data = ""
        num = 0

        while True:
                while ser.inWaiting() > 0:
                        data += ser.read(ser.inWaiting())
                if data != "":
                        print data
                        gnggaIndex = data.find("GNGGA")
                        if gnggaIndex != -1:
                                gnggaStart = gnggaIndex+5
                                gnggaEnd = data.find("*",gnggaStart)
                                gngga = data[gnggaStart:gnggaEnd]
                                northIndex = gngga.find("N")
                                northStart = northIndex-12
                                northEnd = northIndex-1
                                north = gngga[northStart:northEnd]
                                eastIndex = gngga.find("E")
                                eastStart = eastIndex-12
                                eastEnd = eastIndex-1
                                east = gngga[eastStart:eastEnd]
                                if north != -1:
                                        if east != -1:
                                                northDegrees = float(north[0:2])
                                                northMinutes = float(north[2:])/60
                                                northValue = northDegrees+northMinutes
                                                northValueAsString = str(northValue)
                                                eastDegrees = float(east[0:2])
                                                eastMinutes = float(east[2:])/60
                                                eastValue = eastDegrees+eastMinutes
                                                eastValueAsString = str(eastValue)
                                                print " "
                                                print "N", northValue
                                                print "E", eastValue
                                                print " "
                                                POINTS.savePoint(northValueAsString,eastValueAsString)
                        if  num < 4:    # the string have ok
                                print num
                                time.sleep(0.5)
                                ser.write(W_buff[num+1])
                                num =num +1
                        if num == 4:
                                time.sleep(0.5)
                                ser.write(W_buff[4])
                        data = ""

#MAIN
#start()
