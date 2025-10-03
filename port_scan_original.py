import socket

# Basic user interface header
print(r""" 
______          _     _____                                   _   _  ____ 
| ___ \        | |   /  ___|                                 | | | |/ ___|
| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __  | | | / /___ 
|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__| | | | | ___ \
| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |    \ \_/ | \_/ |
\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|     \___/\_____/
                                                                          
                                                                          """)
print("\n****************************************************************")
print("\n* https://beaubremer.com *")
print("\n****************************************************************")

# Get the target host and port range from the user
target_host = input("Enter the target host to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Print a status message showing the target host and port range
print(f"Scanning {target_host} from port {start_port} to port {end_port}...\n")

# Loop over the port range and attempt to connect to each port
for port in range(start_port, end_port+1):
    try:
        # Create a new socket object and attempt to connect to the target host and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target_host, port))

        # Check if the connection was successful (i.e., the port is open)
        if result == 0:
            print(f"Port {port} is open")

        # Close the socket connection
        s.close()

    except KeyboardInterrupt:
        # Allow the user to exit the script using Ctrl-C
        print("\nExiting due to user interrupt")
        break

    except socket.error:
        # Handle any socket errors that occur
        print(f"Could not connect to port {port}")

# Print a status message indicating that the scan is complete
print(f"\nScan of {target_host} is complete.")
102
