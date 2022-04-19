
import logging

# Logging
# Log dados da simulação
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO, filemode='w'):
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Log dados da simulação
logger_data = setup_logger('logger_data', 'simulacao-aeroporto-data.log')
logger_data.setLevel(logging.INFO)
# Log comunicação entre aviao e torre de controle
logger_com = setup_logger('logger_com', 'simulacao-aeroporto-com.log')
logger_com.setLevel(logging.INFO)
