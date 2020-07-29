from datetime import datetime


class Logger:
    def __init__(self, module: str = ""):
        self.module = module

    @staticmethod
    def get_time():
        return datetime.now().strftime("%d.%m.%Y %H:%M.%S")

    def core(self, text: str, end='\n', start='\n'):
        print(start + f"\033[34m[{self.get_time()} CORE]: \033[35m["+self.module+"]\033[0m \033[34m"+text+"\033[0m\n",
              end=end)
        return self

    def info(self, text: str, start="", end="\n"):
        print(start + f"\033[32m[{self.get_time()} INFO]\033[0m: \033[35m[" + self.module + "]\033[0m " + text,
              end=end)
        return self

    def warn(self, text: str, start="", end="\n"):
        print(start + f"\033[33m\033[5m[{self.get_time()} WARN]\033[0m: \033[35m[" + self.module + "]\033[0m " + text,
              end=end)
        return self

    def error(self, text: str, start="", end="\n"):
        print(start + f"\033[31m\033[6m[{self.get_time()} ERROR]\033[0m:\033[35m[" + self.module + "]\033[0m " + text,
              end=end)
        return self
