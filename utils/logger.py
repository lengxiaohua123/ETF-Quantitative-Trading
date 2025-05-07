import logging
import yaml

def setup_logger(config_path="config/logging.yaml"):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)
    logger = logging.getLogger()
    return logger