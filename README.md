et-7017-simulator
================

Set up for a Modbus TCP server that simulates an IoT device model ET-7017

## Getting started

### Set up the enviroment

```bash

python3 -m vnev env
source env/bin/activate

```

### Install the necessary libraries

```bash
pip install pyModbusTCP gunicorn
```

### Start the app

```bash
python3 app.py 
```

### How to use the app 
When you start the program, you will receive the message "Server is online!". The default IP address and port are "127.0.0.1" and "5020".
After this you're good to go!

### Controller used for simulation

-  [ET-7017 controller](https://www.icpdas.com/en/product/ET-7017)
