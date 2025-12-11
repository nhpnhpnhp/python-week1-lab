from datetime import datetime

class LogEntry:
    def __init__(self, message):
        self.timestamp = datetime.now()
        self.message = message
    def display_info(self) :
        print(self.message)
class ErrorLog(LogEntry):
    def __init__(self, message, error_code = 500) :
        super().__init__(message)
        self.error_code = error_code
    def display_info(self):
        print('[URGENT] ' + self.message)
class InfoLog(LogEntry):
    def display_info(self):
        print('[NORMAL] ' + self.message)