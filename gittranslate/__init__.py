import logging.config
import pathlib

logging_config_file_path = pathlib.Path(__file__).parent.absolute() / 'config' / 'logging_config.ini'
logging.config.fileConfig(logging_config_file_path)
