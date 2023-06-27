import logging
import os
import sys
import time
import datetime
import requests
import pytz

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

web_request = requests_get_call(f"{os.environ['RPC_URL']}/genesis")
current_height = int(requests_get_call(f"{os.environ['RPC_URL']}/status")["result"]["sync_info"]["latest_block_height"])
upgrade_height = int(os.environ["UPGRADE_HEIGHT"])
average_block_time = float(os.environ["AVERAGE_BLOCK_TIME"])
if web_request:
    logger.log.info("Web Request: Success")
    voting_period = int(os.environ["VOTING_PERIOD"])
    voting_period = voting_period
    total_number_of_blocks_for_upgrade = upgrade_height - current_height
    total_seconds_for_upgrade = float(total_number_of_blocks_for_upgrade) * average_block_time
    logger.log.info(f"VOTING PERIOD: {voting_period}")
    logger.log.info(f"UPGRADE_HEIGHT: {upgrade_height}")
    logger.log.info(f"CURRENT_HEIGHT: {current_height}")
    logger.log.info(f"AVERAGE BLOCK TIME: {average_block_time}")
    logger.log.info(f"BLOCKS BETWEEN CURRENT BLOCK AND UPGRADE BLOCK: {total_number_of_blocks_for_upgrade}")
    logger.log.info(f"TOTAL SECONDS FOR UPGRADE: {total_seconds_for_upgrade}")
    if total_seconds_for_upgrade > voting_period:
        logger.log.info("UPGRADE HEIGHT BEYOND VOTING PERIOD CHECK: PASS")
    else:
        logger.log.info("UPGRADE HEIGHT BEYOND VOTING PERIOD CHECK: FAILURE")
        sys.exit(2)
    current_time = time.time()
    end_time = current_time + total_seconds_for_upgrade
    end_time_object = datetime.datetime.fromtimestamp(end_time)
    utc_dt = end_time_object.astimezone(pytz.UTC)
    logger.log.info(f"UPGRADE WILL HAPPEN UTC: {str(utc_dt)}")
else:
    logger.log.critical("FAILED:TO:GET:GENESIS")
    sys.exit(2)
GITHUB_ENV = open(os.environ["GITHUB_ENV"], "a+")
GITHUB_ENV.write(f"UPGRADE_DATE={utc_dt}")
GITHUB_ENV.close()
