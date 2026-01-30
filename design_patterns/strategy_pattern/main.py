from log_strategies import ConsoleLogger, FileLogger, CloudLogger
from processor import DataProcessor


if __name__ == '__main__':
    data = ['apple', 'banana', 'cherry']

    print("Using ConsoleLogger:")
    console_logger = ConsoleLogger()
    processor1 = DataProcessor(console_logger)
    processor1.process_data(data)

    print("\nUsing FileLogger:")
    file_logger = FileLogger()
    processor2 = DataProcessor(file_logger)
    processor2.process_data(data)

    print("\nUsing CloudLogger:")
    cloud_logger = CloudLogger()
    processor3 = DataProcessor(cloud_logger)
    processor3.process_data(data)