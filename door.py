import argparse
import signal
import sys
import time
import logging
import datetime
import calendar
import worktime

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
signal.signal(signal.SIGINT, exithandler)

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )
rx = RFDevice(27)
rx.enable_rx()
tx = RFDevice(17)
tx.enable_tx()
timestamp = None
logging.info("Listening for codes on GPIO 27")
while True:
    if worktime.timecalendar():
        if rx.rx_code_timestamp != timestamp:
            timestamp = rx.rx_code_timestamp
            if rx.rx_code==15523:
                logging.info( " 收到门铃 " + str(rx.rx_code))
                logging.info( "\033[40;32;1m工作时间内开门\033[0m")
                for i in range (5):
                    tx.tx_code(opendoorcode, protocol, pulselength)
                    time.sleep(0.1)
    else:
         time.sleep(60)
rx.cleanup()
tx.cleanup()
