from logger_interface import LoggerStrategy


class ConsoleLogger(LoggerStrategy):
    def log(self, message: str) -> None:
        print(message)


class FileLogger(LoggerStrategy):
    def log(self, message: str) -> None:
        with open('sys_log.txt', 'a') as sys_file:
            sys_file.write(message + '\n')


class CloudLogger(LoggerStrategy):
    def log(self, message: str) -> None:
        print(f'Pushing to cloud: {message}')