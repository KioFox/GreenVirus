#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = 9101527

API_HASH = 3d860e0047f2098289ec4eca8649b7da

BOT_TOKEN = 2095742657:AAHhESyW6ic8FpVr4lJ7GsbhkR9sXsw3X2g

DB_URI = https://github.com/TeamUltroid/Ultroid

USER_SESSION = 1ApWapzMBu26jYooDIGc_pul7j3hpgRdO_HQHDpPwx5Ff_qERAd4kceCS7ikYbN2ijI4ZbuvNALwEV8wCW6Zfi7BbF3G0nZySA4f2S6lnvCp4v-yvmqJw1k3s3mpNwy466Te5o3YDOfjrYESaLhAwpeDj_C6kp9Gr0PH6uZHeL5COWfZd8stfVfT9nGGMLeNAjLz2rdLtRnJle1n-7eIyci-LkF07ZjrulO-oj2Zjcjf7nlUtbd81QGIzrmeHyPzv4vSxf08en9kACToFLbpi_aJ5DM1s15hnTi7BDJuQPzxOhZ1khWtuFwHj6NC1Z59yqKwj5FVfwQ5DYOmF-KxIZsxsLKakkBw=

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
