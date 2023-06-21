import logging
import os
import statistics
import sys
import time

import requests
from dateutil.parser import parse


class Logger:
    def __init__(self):
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.log.addHandler(self.handler)


logger = Logger()


def requests_get_call(url):
    try:
        web_request = requests.get(url).json()
    except Exception as e:
        logger.log.error(str(e))
        web_request = None
    return web_request


logger.log.info("START CALCULATING AVERAGE BLOCK TIME")
date_objects = []
web_request = requests_get_call(f"{os.environ['RPC_URL']}/status")
if web_request:
    logger.log.info("Web Request: Success")
    LATEST_BLOCK_HEIGHT = int(web_request["result"]["sync_info"]["latest_block_height"])
    STARTING_SAMPLE_BLOCK_HEIGHT = LATEST_BLOCK_HEIGHT - int(os.environ["AVG_TIME_SAMPLE_SIZE"])
    for block_height in range(STARTING_SAMPLE_BLOCK_HEIGHT, LATEST_BLOCK_HEIGHT):
        logger.log.info(f"LOOKING UP HEIGHT: {block_height}")
        web_request = requests_get_call(f"{os.environ['RPC_URL']}/block?height={block_height}")
        if web_request:
            logger.log.info("BLOCK WEB REQUEST: SUCCESS")
            date_object = parse(web_request["result"]["block"]["header"]["time"])
            date_objects.append(date_object)
        else:
            logger.log.critical("WEB REQUEST: FAILED")
            sys.exit(2)
        time.sleep(.3)
else:
    logger.log.critical("Web Request: Failed")
    sys.exit(2)

first = True
last_date_object = None
time_differences_between_block = []
for date_object in date_objects:
    if first:
        last_date_object = date_object
        first = False
        continue
    else:
        time_difference = date_object - last_date_object
        last_date_object = date_object
        time_difference_between_block = time_difference.total_seconds()
        logger.log.info(f"Difference in seconds: {time_difference_between_block}")
        time_differences_between_block.append(time_difference_between_block)

average_block_time = statistics.mean(time_differences_between_block)
logger.log.info(f"AVERAGE_BLOCK_TIME: {average_block_time}")
GITHUB_ENV = open(os.environ["GITHUB_ENV"], "a+")
GITHUB_ENV.write(f"AVERAGE_BLOCK_TIME={average_block_time}")
GITHUB_ENV.close()
