# Jorik Pfeiffer 2025
# https://github.com/jojopipe/PyLog

import datetime
import os
os.system('')

# global vars:
__log_file__ = None
__no_log__ = False
__everything_to_file__ = False

# functions:

def no_log(override=True) -> None:
    """
    turn off/on all logging
    :param override: value to set global no_log parameter to
    :return:
    """
    global __no_log__
    __no_log__ = override

def always_to_file(override=True) -> None:
    """
        makes every logger call write its message into the specified log file
    :param override: value to set override to
    """
    global __everything_to_file__
    __everything_to_file__ = override

def reset_all_parameters() -> None:
    """
    resets all global logger parameters
    """
    global __log_file__
    global __no_log__
    global __everything_to_file__
    __log_file__ = None
    __no_log__ = False
    __everything_to_file__ = False

def set_log_file(file_path: str) -> None:
    """
    sets the file path that log messages are written to
    :param file_path: file to write log messages to
    :return:
    """
    global __log_file__
    __log_file__ = file_path
    return

def __write_to_file__(message: str) -> None:
    global __log_file__
    assert(__log_file__ is not None)
    with open(__log_file__, "a") as file:
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"{now_time}: {message}\n"
        file.write(output)
    return

def info(message: str, to_file = False) -> None:
    """
    info logger call\n
    prints info message to the standard output
    :param message: message to log
    :param to_file: message will be written to log file, can be overridden by always_to_file()
    """
    if __no_log__:
        return
    output = f"[i] {message}"
    if __everything_to_file__ or to_file:
        __write_to_file__(output)
    print(output)
    return

def okay(message: str, to_file = False) -> None:
    """
    okay logger call\n
    prints okay message to the standard output in green color
    :param message: message to log
    :param to_file: message will be written to log file, can be overridden by always_to_file()
    """
    if __no_log__:
        return
    output = f"[k] {message}"
    if __everything_to_file__ or to_file:
        __write_to_file__(output)
    #os.system('')
    print("\033[92m{}\033[00m" .format(output))
    return

def warning(message: str, to_file = False) -> None:
    """
    warning logger call\n
    prints warning message to the standard output in yellow color
    :param message: message to log
    :param to_file: message will be written to log file, can be overridden by always_to_file()
    """
    if __no_log__:
        return
    output = f"[w] {message}"
    if __everything_to_file__ or to_file:
        __write_to_file__(output)
    #os.system('')
    print("\033[93m{}\033[00m" .format(output))
    return

def error(message: str, to_file = False) -> None:
    """
    error logger call\n
    prints error message to the standard output in red color
    :param message: message to log
    :param to_file: message will be written to log file, can be overridden by always_to_file()
    """
    if __no_log__:
        return
    output = f"[e] {message}"
    if __everything_to_file__ or to_file:
        __write_to_file__(output)
    #os.system('')
    print("\033[91m{}\033[00m" .format(output))
    return

def extra(message: str, to_file = False) -> None:
    """
    extra logger call\n
    prints extra message to the standard output in cyan color
    :param message: message to log
    :param to_file: message will be written to log file, can be overridden by always_to_file()
    """
    if __no_log__:
        return
    output = f"[x] {message}"
    if __everything_to_file__ or to_file:
        __write_to_file__(output)
    #os.system('')
    print("\033[96m{}\033[00m" .format(output))
    return