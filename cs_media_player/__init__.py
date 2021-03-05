import logging
print(f'configuring logger')
logging.basicConfig(filename='event.log',
                    filemode='a',
                    format='%(asctime)s, '
                           '%(levelname)s, '
                           '%(module)s, '
                           '%(funcName)s, '
                           '%(lineno)d, '
                           '%(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info(f'importing \'{__name__}\'')
print(f'importing \'{__name__}\'')
