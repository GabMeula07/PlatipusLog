import sys
import yaml


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
        

def main():
    if len(sys.argv) < 2:
        print(''' commands: \n   init - Initialize platiputs environment
        ''')
        return

    cmd = sys.argv[1]

    if cmd == "init":
        print(f"{"-"*50}")

        print(
        '''
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

        ''')
        print(f"{"-"*50}")

        print("Init PLatipusLogger...")
        print("Create a config file...")
        create_config_file()
        print("Create a config file: OK ")

    else:
        print(f"Comand '{cmd}' not found")