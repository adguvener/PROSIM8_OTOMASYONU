import serial
import time

def send_command(ser, command):
    ser.write((command + "\r\n").encode('utf-8'))
    response = ser.readline().decode('utf-8').strip()
    print(f"Response to {command}: {response}")

def listen_for_data(ser):
    
    response = ser.readline().decode('utf-8').strip()
    if response:
        print(f"Incoming data: {response}")


if __name__ == "__main__":
    # Define your commands here
    command_string = "EXIT-LOCAL-REMOTE-IDENT-ECGRUN=TRUE-NSRA=090-"
    
    commands = command_string.replace('-', ', ').split(", ")
    # Initialize serial connection
    ser = serial.Serial("COM16", 115200, timeout=1)
    
    # Start the listening thread if DREADY is in the commands
    if "DREADY" in commands:
        listen_for_data(ser)
    
    # Iterate over the commands and send them
    for command in commands:
        send_command(ser, command)
        time.sleep(0.5)
    
    # The script will not reach this point unless you add a condition to stop the timer
    # ser.close()
