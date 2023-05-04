import lib27gn950
import hid
import time

if __name__ == "__main__":

	while True:
		monitors = lib27gn950.find_monitors()
		devs = []

		for monitor in monitors:
			dev = hid.Device(path=monitor['path'])
			dev.model = monitor['model']
			devs.append(dev)

		cmd = "turn_off"

		if cmd in lib27gn950.control_commands.keys():
			lib27gn950.send_command(lib27gn950.control_commands[cmd], devs)

		time.sleep(1)