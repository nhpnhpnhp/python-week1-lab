import logging
from models import *
logging.basicConfig(filename = "pipeline_error.log", level = logging.ERROR)

class LogFormatError(Exception):
    pass

def parse_log_line(line):
    try:
        log_type, message = line.split(":", maxsplit=1)
        if(log_type == 'ERROR'):
            return ErrorLog(message)
        elif(log_type == 'INFO'):
            return InfoLog(message)
        else :
            return LogEntry(message)
    except ValueError:
        logging.error(f"Missing separator ':'. Content: {line}")
        raise LogFormatError(f"Missing separator ':'. Content: {line}")
def read_log_file(file_path):
    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")

def main():
    file_path = '../data/server.log'
    processed_logs = []
    for line in read_log_file(file_path):
        try:
            processed_logs.append(parse_log_line(line))
        except LogFormatError:
            continue
    logs_messages = [log.message for log in processed_logs if isinstance (log, ErrorLog)]
    print(f'Total success logs : {len(processed_logs)}')
    print('List of Error Messages')
    for log in logs_messages:
        print(log)

if __name__ == "__main__":
    main()