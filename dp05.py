class Logger(object):
    class __Logger:
        def __init__(self):
            self.file_name = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)

        def _write_log(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warning(self, msg):
            self._write_log("WARNING", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()

        return Logger.instance
