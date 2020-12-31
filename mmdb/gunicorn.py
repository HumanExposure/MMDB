import logging
import multiprocessing

from mmdb.environment import env
from mmdb.settings import LOGGING

# Default configuration
bind = ":" + env.MMDB_PORT
workers = multiprocessing.cpu_count() * 2 + 1
logconfig_dict = LOGGING
access_log_format = '"%(r)s" %(s)s %(b)s'

# Override/set any configuration variable with environment variables
locals().update(env.GUNICORN_OPTS)


def on_starting(server):
    logger = logging.getLogger("django")
    if env.DEBUG:
        logger.warning("Running in DEBUG mode")
    if "*" in env.ALLOWED_HOSTS:
        logger.warning("Host checking is disabled (ALLOWED_HOSTS is set to accept all)")
