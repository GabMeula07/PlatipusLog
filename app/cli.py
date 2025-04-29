import sys
import yaml

from app.models.logger import Base

from sqlalchemy import create_engine

def create_root_dir(config_url):
    try: 
        os.makedirs(config_url, exist_ok=True)
    except Exception as e: 
        print(f"Error in create folder: {e}")

def create_config_file(): 
    # default config
    config = {
        "database": {
            "url": "sqlite:///platipuslogs.db"  
        },
        "logs": {
            "root_path": "logs/"  
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

    with open("platipus.config.yaml", "w") as file:
            yaml.dump(config, file, default_flow_style=False)
    
    return config
        
def create_database(config_url):
    print("Criando conexão com o banco...")
    engine = create_engine(config_url)
    print("Migrando Models...")
    Base.metadata.create_all(engine)

def read_config():
    try:
        with open("platipus.config.yaml", "r") as file:
            config = yaml.safe_load(file)

    except FileNotFoundError:
        print(f"Error: platipus.config.yaml not found.")
        return None

    return config
     



def main():
    if len(sys.argv) < 2:
        print(''' commands: \n   init - Initialize platiputs environment
        ''')
        return

    cmd = sys.argv[1]

    if cmd == "init":
        print(f"{"-"*50}")

        print(
        '''\033[94m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠁⠀⠀⠀⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣠⣾⡋⢻⡄⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠉⠛⢦⣄⠀⠀⠀
⠀⣠⣴⠖⠛⠋⠉⠁⠀⠹⣬⣻⠆⠈⠁⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠹⣆⣀⣀⡀⠀⠀⠀⠈⠳⢦⡀
⢸⡟⠉⣴⠀⠀⠀⠀⢀⣤⢟⣿⠀⠀⠀⠀⠀⠀⣆⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣀⣼⠷⠀⠀⠀⢀⣽⠀⠈⠉⠛⠒⠶⠶⠒⠛⠁
⠈⠳⣆⡀⠀⣀⣤⣶⠿⠟⠋⠉⠳⢦⣤⣀⣠⡾⠋⠀⠀⢠⣾⣀⣤⡤⠶⠚⣿⡿⣿⡄⡄⣰⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣴⣿⢀⠀⣠⡴⠚⠉⠀⠀⠀⠀⠀⠀⠈⢿⣧⣸⣇⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣯⡾⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
        print(
        '''
           _       _                         
          | |     | |                        
     _ __ | | __ _| |_ _   _ _ __  _   _ ___ 
    | '_ \| |/ _` | __| | | | '_ \| | | / __|
    | |_) | | (_| | |_| |_| | |_) | |_| \__ \ 
    | .__/|_|\__,_|\__|\__, | .__/ \__,_|___/
    | |                 __/ | |              
    |_|                |___/|_| 
    \033[00m
        ''')
        print(f"{"-"*50}")

        print("\nInit PLatipusLogger...")
        print("Create a config file...")
        config = create_config_file()
        print("Create a config file: OK ")
        print("Create a Root Log Dir...")
        create_root_dir(config["logs"]["root_path"])
        print("Create a Root Log Dir: OK")

        create_database(config["database"]["url"])
        print("Database: OK")

    elif cmd == "restart":
        config = read_config()
        create_database(config["database"]["url"])
        print("Database: OK")

    else:
        print(f"Comand '{cmd}' not found")

    