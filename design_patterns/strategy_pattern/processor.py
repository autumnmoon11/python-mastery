from logger_interface import LoggerStrategy


class DataProcessor:
    def __init__(self, logger: LoggerStrategy):
        self.logger = logger

    def process_data(self, data_list: list) -> None:
        self.logger.log('Starting list iteration')
        for item in data_list:
            self.logger.log(f'Processing item: {item}')
        self.logger.log('Ended list iteration')
