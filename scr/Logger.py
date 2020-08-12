import os

from datetime import datetime


class LogInFile:
    def __init__(self,
                 style: str,
                 module: any,
                 need_file_log: bool,
                 patch: str = "./",
                 name: str = "LOG_%d",
                 ext: str = ".log"
                 ) -> None:

        self.patch = patch.replace(":", "").replace(" ", "_")
        self.name = name.replace(":", "").replace(" ", "_")
        self.ext = ext.replace(":", "").replace(" ", "_")

        self.module = module.replace(":", "").replace(" ", "_")
        self.style = style  # Base style

        self.need_file_log = need_file_log  # Are you need file?

        self.is_find_file: bool = False
        self.final_patch: str = ""

    def find_file(self):
        if not self.is_find_file:
            final_patch: str = ""
            find = False
            i = 0
            while not find:
                final_patch = self.patch.replace("%module", self.module) + \
                              self.name.replace("%module", self.module) % i + \
                              self.ext
                if not os.path.exists(final_patch):
                    try:
                        with open(final_patch, "w"):
                            find = True
                    except FileNotFoundError:
                        os.makedirs(os.path.dirname(final_patch))
                else:
                    i += 1
            self.is_find_file = True
            self.final_patch = final_patch

    def style_parse(self, state, text) -> str:
        set_module = self.style.replace("%module", self.module)
        set_state = set_module.replace("%state", state)
        set_text = set_state.replace("%text", text)
        set_time = datetime.now().strftime(set_text)
        return set_time

    def save(self, state, text) -> None:
        self.find_file()
        if self.need_file_log:
            text = self.style_parse(state, text) + "\n"
            with open(self.final_patch, "a") as f:
                f.write(text)


class Logger:
    def __init__(self, module: any = "log",  # %module

                 file_save: bool = False,  # If you need save log in file, use True
                 file_style: str = "[%d.%m.%Y %H:%M.%S %state]: [%module] %text",  # Text style in file
                 file_patch: str = "./logs/%module/",
                 file_name: str = "%module_%d",
                 file_ext: str = ".log"

                 ) -> None:
        self.module = str(module)

        self.to_file: LogInFile = LogInFile(file_style, module, file_save, file_patch, file_name, file_ext)

    @staticmethod
    def get_time() -> str:
        return datetime.now().strftime("%d.%m.%Y %H:%M.%S")

    def core(self, text: any, end='', start='\n'):
        print(
            start + f"\033[34m[{self.get_time()} CORE]: \033[35m[" + self.module + "]\033[0m \033[34m" +
            str(text) + "\033[0m\n", end=end)
        self.to_file.save("CORE", text)
        return self

    def info(self, text: any, start="", end="\n"):
        print(start + f"\033[32m[{self.get_time()} INFO]\033[0m: \033[35m[" + self.module + "]\033[0m " +
              str(text), end=end)
        self.to_file.save("INFO", text)
        return self

    def warn(self, text: any, start="", end="\n"):
        print(start + f"\033[33m\033[5m[{self.get_time()} WARN]\033[0m: \033[35m[" + self.module + "]\033[0m " +
              str(text), end=end)
        self.to_file.save("WARN", text)
        return self

    def error(self, text: any, start="", end="\n"):
        print(start + f"\033[31m\033[6m[{self.get_time()} ERROR]\033[0m:\033[35m[" + self.module + "]\033[0m " +
              str(text), end=end)
        self.to_file.save("ERROR", text)
        return self


def test(log: Logger) -> None:
    t = time.time()
    log.core("Text")
    log.info("Text")
    log.warn("Text")
    log.error("Text")
    log.info(f"test ended, work time: {time.time() - t}")


if __name__ == '__main__':
    import time
    t = time.time()
    Logger0 = Logger(
        "Simple"
    )

    Logger1 = Logger(
        "Simple and file save",
        file_save=True
    )

    Logger2 = Logger(
        "Simple, save and restyle",
        file_save=True,
        file_style="%state: %module %text",
    )
    Logger3 = Logger(
        module="All settings:",
        file_save=True,
        file_style="[%d.%m.%Y %H:%M.%S %state]: [%module] %text",
        file_patch="./logs/%module/",
        file_name="%module_%d",
        file_ext=".log"
    )

    test(Logger0)
    test(Logger1)
    test(Logger2)
    test(Logger3)
    Logger0.info(f"Script ended, work time: {time.time() - t}")
