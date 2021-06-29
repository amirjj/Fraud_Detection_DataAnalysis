# python imports
from lxml import etree
import logging.config

# project imports
from models.integration import APICall
from extensions import db
from config import DefaultConfig

U_LOGFILE_NAME = DefaultConfig.LOG_LOCATION
U_LOGFILE_SIZE = 10 * 1024 * 1024
U_LOGFILE_COUNT = 20
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s.%(msecs)03d] %(levelname)8s [%(name)s:%(filename)s:%(lineno)s %(process)d %(thread)d - %(funcName)20s()] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'api_call_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': U_LOGFILE_NAME,
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'api_call_log': {
            'handlers': ['api_call_file'],
            'propagate': True,
            'level': 'ERROR',
        },
    }
}


def minify_xml(xml_string):
    parser = etree.XMLParser(remove_blank_text=True, recover=True)
    elem = etree.XML(xml_string, parser=parser)
    return etree.tostring(elem, encoding='utf-8')


logging.config.dictConfig(LOGGING)
logger_api_call = logging.getLogger("api_call_log")


def api_call_log(api_name=None, api_url=None, msisdn=None, national_code=None,
                 reserved_field_1=None, reserved_field_2=None, reserved_field_3=None, request=None, request_time=None,
                 response=None, response_time=None, insert_to_db=False):
    if insert_to_db:
        api_call = APICall(api_name=api_name,
                           api_url=api_url,
                           msisdn=msisdn,
                           national_code=national_code,
                           reserved_field_1=reserved_field_1,
                           reserved_field_2=reserved_field_2,
                           reserved_field_3=reserved_field_3,
                           request=request,
                           request_time=request_time,
                           response=response,
                           response_time=response_time)
        db.session.add(api_call)
        db.session.commit()

    logger_api_call.info({'api_name': api_name, 'api_url': api_url, 'msisdn': msisdn, 'national_code': national_code,
                          'reserved_field_1': reserved_field_1, 'reserved_field_2': reserved_field_2, 'reserved_field_3': reserved_field_3,
                          'request': request, 'response': response, 'request_time': request_time, 'response_time': response_time})


