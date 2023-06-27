import logging
import os
import sys
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

upgrade_date_object = datetime.datetime.strptime(os.environ["UPGRADE_DATE"], "%m/%d/%Y %H:%M")
now = datetime.datetime.now()
utc_now = now.astimezone(pytz.UTC)
utc_future = upgrade_date_object.astimezone(pytz.UTC)
difference = utc_future - utc_now
seconds_difference = difference.total_seconds()
blocks_within_available_seconds = float(seconds_difference) / float(os.environ["AVERAGE_BLOCK_TIME"])
current_height = int(requests_get_call(f"{os.environ['RPC_URL']}/status")["result"]["sync_info"]["latest_block_height"])
upgrade_height = current_height + int(blocks_within_available_seconds)
logger.log.info(f"UPGRADE_HEIGHT_CALCULATED: {upgrade_height}")
GITHUB_ENV = open(os.environ["GITHUB_ENV"], "a+")
GITHUB_ENV.write(f"UPGRADE_HEIGHT={upgrade_height}")
GITHUB_ENV.close()