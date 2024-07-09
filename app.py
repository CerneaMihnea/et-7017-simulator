from pyModbusTCP.server import ModbusServer
import random
import time

listen_address = "127.0.0.1"

def convert_data_dusk_sensor(value):
    return int((abs(-10-value) * 6 / 21)* 1000)

def generate_random_values():
    return [convert_data_dusk_sensor(random.uniform(-10 , 10 ))]


server = ModbusServer(listen_address, 5020, no_block= True)

try:
    server.start()
    print("Server is online!")
    while True:
        server.data_bank.set_input_registers(0, generate_random_values())
        time.sleep(0.5)
except:
    server.stop()
    print("Server is offline!")
