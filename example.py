import pylog

pylog.set_log_file("example.log")
pylog.info("info message example")
pylog.okay("all good", to_file=True)
pylog.warning("hold up, that looks dangerous", to_file=True)
pylog.error("OHMAGAH, WEE WOO WEE WOO, ERROR OCCURED", to_file=True)
pylog.extra("extra cheese please")