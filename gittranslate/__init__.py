import logging.config

logging.config.fileConfig('./gittranslate/config/logging_config.ini')
log = logging.getLogger(__name__)
log.info('Logger Initialized')
