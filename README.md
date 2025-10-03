# Python Network Port Scanner
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](/CONTRIBUTING.md) 
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
[![GitHub issues](https://img.shields.io/github/issues/your-username/py_network_port_scan)](https://github.com/KnowOneActual/py_network_port_scan/issues)


`py_network_port_scan` is a simple and fast multi-threaded TCP port scanner written in Python. This project began as a basic, single-threaded script and has since been updated to become a more efficient and practical command-line tool.

The original script (`port_scan_original.py`) is included to show the project's evolution.

-----

## What It Does

This tool allows you to scan a target host (either an IP address or a domain name) to discover open TCP ports. It reports which ports are open and attempts to grab the service banner to identify what might be running on that port.

## Why This Project Exists

This project began years ago as a simple script to learn the fundamentals of network scanning with Python's socket library. I recently decided to revisit it, applying new knowledge to improve its performance and usability.

The goal was to transform it from a basic, synchronous script into a faster, concurrent, and more user-friendly tool. It serves as a personal example of skill progression and is shared in the hope that it might be useful to others who are learning.

## Features

  * **Concurrent Scanning**: Uses multithreading to scan multiple ports simultaneously, making it significantly faster than a simple loop.
  * **Command-Line Interface**: Implemented with `argparse` for easy use in a terminal or in scripts.
  * **Flexible Port Selection**: Scan a range of ports (e.g., `1-1024`) or specify individual ports (e.g., `22,80,443`).
  * **Banner Grabbing**: Attempts to identify the service running on open ports by grabbing and displaying its banner.
  * **Hostname Resolution**: Automatically resolves domain names to their IP addresses before scanning.

-----

## How to Use It

### Prerequisites

  * Python 3.x

### Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/py_network_port_scan.git
    cd py_network_port_scan
    ```

2.  **Run the script:**
    The script is run from the command line, with the target as a required argument.

    ```bash
    python port_scan_v2.py <target> [options]
    ```

### Options

| Flag          | Argument          | Description                                           | Default   |
|---------------|-------------------|-------------------------------------------------------|-----------|
| `target`      | (required)        | The target host to scan (IP or domain name).          | N/A       |
| `-p`, `--ports` | e.g., "1-200"     | The port range to scan. Can be a range or a comma-separated list. | "1-1024"  |
| `-t`, `--threads` | e.g., "100"       | The number of concurrent threads to use for scanning. | 50        |

### Examples

  * **Scan a target for the most common 1024 ports:**

    ```bash
    python port_scan_v2.py scanme.nmap.org
    ```

  * **Scan a specific port range with 100 threads:**

    ```bash
    python port_scan_v2.py 192.168.1.1 -p 1-500 -t 100
    ```

  * **Scan a few specific ports:**

    ```bash
    python port_scan_v2.py example.com -p 22,80,443,8080
    ```

-----

## Contributing

Contributions are always welcome\! Please see the [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) file for guidelines on how to get involved.

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.