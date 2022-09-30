#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5797423841:AAGJ7dhh96OUOpnzuZpG1sIkg6yDNoMKU4k")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "19987622"))
    API_HASH = os.environ.get("API_HASH", "00d42b460cef01c13d97dad1f417194e")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "21040638").split())
    
