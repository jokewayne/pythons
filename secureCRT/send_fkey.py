# $language = "python"
# $interface = "1.0"

# This script simulates an F3 keypress (VT100 keyboard)

def main():

	# Simulate F3 by sending ESC-OR
	#
	crt.Screen.Send("\033OR")

main()
