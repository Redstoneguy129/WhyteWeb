# __          ___    ___     _________ ________          ________ ____
# \ \        / / |  | \ \   / /__   __|  ____\ \        / /  ____|  _ \
#  \ \  /\  / /| |__| |\ \_/ /   | |  | |__   \ \  /\  / /| |__  | |_) |
#   \ \/  \/ / |  __  | \   /    | |  |  __|   \ \/  \/ / |  __| |  _ <
#    \  /\  /  | |  | |  | |     | |  | |____   \  /\  /  | |____| |_) |
#     \/  \/   |_|  |_|  |_|     |_|  |______|   \/  \/   |______|____/

"""
WhyteWeb HTTP Server Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WhyteWeb is an HTTP Server Library, written in Python, for idiots.

:copyright: (c) 2022 by Cameron Whyte
:license: All Rights Reserved
"""

from .server import *
from .client import *

import logging

logging.getLogger(__name__)
