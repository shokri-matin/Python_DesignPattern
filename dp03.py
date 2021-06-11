class Logger(object):
    class __Logger:
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    instance = None

    def __new__(cls):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()

        return Logger.instance
