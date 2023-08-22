# -*- coding: utf-8 -*-
import datetime
import enum
import os.path
import glob
import sys

from BGLogger.BGConsole import BGC

class ExitController:

    @staticmethod
    def raise_exception(message: str, e: Exception = None):
        if e is None:
            raise Exception(f'FATAL EXCEPTION HAS BEEN RAISED! Message: {message}')
        raise e

    @staticmethod
    def exit(message: str, e: Exception = None):
        sys.exit(1)

class OutputStyle(enum.Enum):
    BOLD = BGC.Param.BOLD
    UNDERLINE = BGC.Param.UNDERLINE
    REGULAR = BGC.Param.NULL

class ExitType(enum.Enum):
    RAISE_EXCEPTION = ExitController.raise_exception
    EXIT = ExitController.exit

class Log:

    __version__ = "1.3.1"
    __github__ = "https://github.com/BelGray/BGLogger"

    def __init__(self, process_name: str, record: bool, return_every_log: bool, output_style: OutputStyle, color: bool):
        self.__color = color
        self.__pattern = "%L -*- %D -*- [%T]   '%M'"
        self.__logs_str = f"---*--- \"{process_name}\" LOGGING RESULT ---*---"
        self.__param = output_style.value
        self.__name = process_name
        self.__record = record
        self.returning = return_every_log

        self.__debugs = 0
        self.__info = 0
        self.__warnings = 0
        self.__errors = 0
        self.__success = 0
        self.__fatal = 0

    def set_log_string_pattern(self, pattern: str):
        """Set log string pattern.
        %L - log Level
        %D - log Date
        %T - log Tag
        %M - log Message
        """
        self.__pattern = pattern

    def save_logs_to_file(self, file_name: str = None, remove_existing: bool = False):
      """Save logs to a TXT file"""
      if self.__record:
        if file_name is None:
            file_name = f'{self.__name}_log_result'
        file_name = file_name.split('.')[0]
        if os.path.exists(file_name + '.txt'):
            if remove_existing:
                os.remove(file_name + '.txt')
            else:
                num = len(glob.glob(file_name + "*"))
                file_name = file_name + str(num)
        with open(file_name + '.txt', 'w', encoding='utf-8') as f:
            f.write(self.__logs_str)
            f.write(f"\n\n----------- *** -----------\nDEBUG LOGS: {self.__debugs}\nINFO LOGS: {self.__info}\nWARNING LOGS: {self.__warnings}\nERROR LOGS: {self.__errors}\nSUCCESS LOGS: {self.__success}\nFATAL LOGS: {self.__fatal}")
            f.write(f"\n\n\n### SAVE DATE: {datetime.datetime.now()} ###")
            f.close()
      else:
        self.e('save_logs_to_file', 'It was not possible to save logs to a file, since the recording was disabled when creating the logging object')

    def d(self, tag: str, message: str):
        """Debug log"""
        self.__debugs += 1
        log_time = datetime.datetime.now()
        LVL = "DEBUG"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.CYAN if self.__color else None)
        if self.returning:
            return log_str

    def i(self, tag: str, message: str):
        """Info log"""
        self.__info += 1
        log_time = datetime.datetime.now()
        LVL = "INFO"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.BLUE if self.__color else None)
        if self.returning:
            return log_str

    def w(self, tag: str, message: str):
        """Warning log"""
        self.__warnings += 1
        log_time = datetime.datetime.now()
        LVL = "WARNING"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.MUSTARD if self.__color else None)
        if self.returning:
            return log_str

    def e(self, tag: str, message: str):
        """Error log"""
        self.__errors += 1
        log_time = datetime.datetime.now()
        LVL = "ERROR"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.RED if self.__color else None)
        if self.returning:
            return log_str

    def s(self, tag: str, message: str):
        """Success log"""
        self.__success += 1
        log_time = datetime.datetime.now()
        LVL = "SUCCESS"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.GREEN if self.__color else None)
        if self.returning:
            return log_str

    def f(self, tag: str, message: str, exit_type: ExitType, exception: Exception = None):
        """Fatal log. After calling this log, the program will be stopped"""
        self.__fatal += 1
        log_time = datetime.datetime.now()
        LVL = "FATAL"
        log_str = "\n" + self.__pattern.replace('%L', LVL).replace('%D', str(log_time)).replace('%T', tag).replace('%M', message)
        if self.__record:
            self.__logs_str += log_str
        BGC.write(log_str, param=self.__param, color=BGC.Color.CRIMSON if self.__color else None)
        exit_type(message, exception)
