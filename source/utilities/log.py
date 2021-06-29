# python imports
import logging.config

# project imports
from flask import request

report_logger = logging.getLogger("report_logger")


def report(msg):
    ip = request.headers.get('x-forwarded-for', request.remote_addr)
    report_logger.info('[ip: %s] [url: %s] %s' % (ip, request.url, msg))
