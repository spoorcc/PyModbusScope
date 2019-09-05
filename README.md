# PyModbusScope

A little toy project to control [ModbusScope](https://github.com/jgeudens/modbusscope) from the commandline.

## Installing
1. Make sure [ModbusScope](https://github.com/jgeudens/modbusscope) is installed.
2. Install script in a venv
```
python -m venv venv
venv\Scripts\Activate.ps1
pip install -e .
```

## Usage

### Logging with given mbs file for 5 seconds
```python
from time import sleep
from pymodbusscope import ModbusScope

mbs = ModbusScope()
mbs.load_project('myproject.mbs')
mbs.start_logging()
sleep(5)
mbs.stop_logging()
```