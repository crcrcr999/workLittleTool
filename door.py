import argparse
import signal
import sys
import time
import logging
import datetime
import calendar

from rpi_rf import RFDevice

rx = None
tx = None
opendoorcode=1189572
protocol=1
pulselength=360
# pylint: disable=unused-argument
def exithandler(signal, frame):
    rx.cleanup()
    tx.cleanup()
    sys.exit(0)
def timecalendar():
    currentdate = datetime.date.today()
    #工作日13-20
    #节假日12-21
    workrange=[13,20]
    holidayrange=[12,21]
    isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
    nowhour = datetime.datetime.now().hour
    currentday =calendar.weekday(currentdate.year,currentdate.month,currentdate.day)
    if currentday >= 4:
        return isworktime(nowhour,holidayrange)
    else:
        return isworktime(nowhour,workrange)
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )
signal.signal(signal.SIGINT, exithandler)
rx = RFDevice(27)
rx.enable_rx()
tx = RFDevice(17)
tx.enable_tx()
timestamp = None
logging.info("Listening for codes on GPIO 27")
while True:
    if rx.rx_code_timestamp != timestamp:
        timestamp = rx.rx_code_timestamp
        if rx.rx_code==15523:
            logging.info( " 收到门铃 " + str(rx.rx_code))
            if timecalendar:
                logging.info( "\033[40;32;1m工作时间内开门\033[0m")
                for i in range (5):
                    tx.tx_code(opendoorcode, protocol, pulselength)
                    time.sleep(0.1)
            else:
                logging.info( "\033[41;37;1m非工作时间内!不开\033[0m")
    time.sleep(0.01)
rx.cleanup()
tx.cleanup()
