# Logger for Python

<p align="center">
    <img src="https://img.shields.io/github/license/SantaSpeen/Logger.Python?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/SantaSpeen/Logger.Python?style=for-the-badge">
</p>

### Installing

* Download this repo
* Init in your project

### Usage

```python
import time
from Logger import Logger

def test(log: Logger) -> None:
    t = time.time()
    log.core("Text")
    log.info("Text")
    log.warn("Text")
    log.error("Text")
    log.info(f"test ended, work time: {time.time() - t}")

# Initialize logger 
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

# Use it!
test(Logger0)
test(Logger1)
test(Logger2)
test(Logger3)
```

### Links!

- [Python](python.org)

- [Link to this project](https://github.com/SantaSpeen/Logger.Python)

- [Author](https://vk.com/id370926160)