# Copyright (c) Prometeo AI, Inc. All rights reserved.


from timeit import default_timer
from datetime import timedelta


class Timer(object):
    """Timer class.
    Source: https://github.com/miguelgfierro/codebase/blob/b761ab0b0b853734fcab18cd1ad958bd70b0f0ab/python/log_base/timer.py
    """

    def __init__(self):
        self._timer = default_timer
        self.interval = 0

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def __str__(self):
        return str(timedelta(seconds=self.interval))

    def start(self):
        """Start the timer."""
        self.init = self._timer()

    def stop(self):
        """Stop the timer. Calculate the interval in seconds."""
        self.end = self._timer()
        self.interval = self.end - self.init
