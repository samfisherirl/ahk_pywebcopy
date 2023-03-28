from pywebcopy import save_webpage, save_website
from pathlib import Path
from os import mkdir

class Save:
    def __init__(self, path):
        self.path = path
        self.config = ""
        self.command = ""
        self.save_path = ""
        self.name = ""
        self.url = ""

    def get_config(self):
        with open(self.path, "r") as f:
            self.config = f.read()
        line = self.config.split(",,")
        self.command = line[0]
        self.save_path = line[2]
        try:
            mkdir(self.save_path)
        except Exception as e:
            print(e)
        self.url = line[1]
        self.name = line[3]
        if "webpage" in self.command:
            self.webpage()
        if "website" in self.command:
            self.website()
        
        
    def webpage(self):
        save_webpage(
        url=f"{self.url}",
        project_folder=f"{self.save_path}",
        project_name=f"{self.name}",
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
        )

        
    def website(self):
        save_website(
        url=f"{self.url}",
        project_folder=f"{self.save_path}",
        project_name=f"{self.name}",
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
        )

if __name__ == "__main__":
    p = Path.cwd()
    config = p / "command.txt"
    s = Save(config)
    s.get_config()
    