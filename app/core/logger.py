
class Logger:
    def __init__(self, name: str):
        self.name = name
        self.modes = {
            "ERROR": '''\033[91m''',
            "WARN": '''\033[93m''',
            "INFO": '''\033[94m'''
        }

    def _printMode(self, mode: str, msg: str):
        print(f"{self.modes[f"{mode}"]}[{self.name.upper()}] {msg}")

    def error(self, msg: str):
        self._printMode("ERROR", msg)
    
    def info(self, msg: str):
        self._printMode("INFO", msg)

    def warn(self, msg: str):
        self._printMode("WARN", msg)