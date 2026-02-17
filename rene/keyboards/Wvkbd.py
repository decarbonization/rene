import subprocess
from typing import override

import psutil

from rene.keyboards.base import Keyboard


class Wvkbd(Keyboard):
    def __init__(self):
        pid = next(
            (item.pid for item in psutil.process_iter() if item.name() == "wvkbd"), None
        )
        if pid is None:
            raise RuntimeError("wvkbd is not running")

        self.pid = pid

    @override
    def show_keyboard(self):
        subprocess.call(["kill", "-SIGUSR1", str(self.pid)])

    @override
    def hide_keyboard(self):
        subprocess.call(["kill", "-SIGUSR2", str(self.pid)])
