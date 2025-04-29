import yaml 
 
from app.core.file_manager import PlatypusFileManager

class Logger:
    def __init__(self, name: str, mode: str):
        allowed_modes = {"testing", "development", "production"}
        if mode not in allowed_modes:
            raise ValueError(f"Invalid Mode: '{mode}'. Modes Available: {', '.join(allowed_modes)}")

        with open('platipus.config.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

        self.name = name
        self.mode = mode
        self.levels = {
            "DEBUG": { "color": 34, "level": 10},
            "INFO": { "color": 94, "level": 20},
            "WARN": { "color": 93, "level": 30},
            "ERROR": { "color": 91, "level": 40},
            "CRITICAL": {"color": 41, "level": 50}
        }

        self.file_manager = PlatypusFileManager(self.config)

    def _get_mode(self)->str:
        return self.mode

    def _log(self, level: str, msg: str):
        color_mode = self.levels[f"{level}"]["color"]
        if self._verify_mode(level=level):
            return
        self.file_manager.insert_row_log_file(
            name=self.name.upper(), 
            mode=level,
            msg=msg
        )
        print(f"\033[{color_mode}m [{self.name.upper()}] {msg}")
        
    def _verify_mode(self, level: str):
        mode = self._get_mode()
        config_level = self.config["modes"][f"{mode}"]["level"]

        if self.levels[config_level]["level"] <= self.levels[f"{level}"]["level"]:
            return False

        return True

    def debug(self, msg: str): self._log("DEBUG", msg)

    def error(self, msg: str): self._log("ERROR", msg)
    
    def info(self, msg: str): self._log("INFO", msg)

    def warn(self, msg: str): self._log("WARN", msg)

    def critical(self, msg: str): self._log("CRITICAL", msg)
