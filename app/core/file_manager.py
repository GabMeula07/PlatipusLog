import os
from datetime import datetime, timezone, date
from pathlib import Path


class PlatypusFileManager:
    def __init__(self, config: dict):
        self.config = config
        self.file_data_format = "%y-%m-%d"
        self.log_data_format = "%Y-%m-%d %H:%M:%S"
        self.root_path = config["logs"]["root_path"]


    def _get_filename(self):
        root_path = Path(self.root_path)
        date_text = datetime.now(timezone.utc)

        log_filename = f"platipus.log.{date_text.strftime(self.file_data_format)}"
        log_file_path = root_path / log_filename 

        return log_file_path


    def _create_log_file(self):
        log_file_path = self._get_filename()

        if not log_file_path.exists():
            try: log_file_path.touch()
            except Exception as e:
                print("Error in create a log file: {e}") 
        

    def insert_row_log_file(self,name:str,  mode: str, msg: str):
        log_file_path = self._get_filename()
        date_text = datetime.now(timezone.utc)

        if not log_file_path.exists():
            self._create_log_file()

        with open(log_file_path, "a") as file:
            file.write(f"{date_text.strftime(self.log_data_format)} [{name}] [{mode}] {msg} \n")


if __name__ == "__main__":
    platfm = PlatypusFileManager(
    config = {
        # default config
        "database": {
            "url": "sqlite:///platipuslogs.db"  
        },
        "logs": {
            "root_path": "./logs"  
        },
        "modes": {
            "production": {
                "level": "WARNING",
                "console": False,
                "file": True,
            },
            "development": {
                "level": "DEBUG",  
                "console": True,
                "file": True,
 
            },
            "testing": {
                "level": "INFO",
                "console": True,
                "file": False,
            }
        }
    }
)
    platfm._create_log_file()