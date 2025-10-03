import socket
import threading
from queue import Queue
import argparse
import sys
from datetime import datetime

# A thread-safe print lock
print_lock = threading.Lock()

def get_banner(s):
    """
    Tries to grab a banner from an open socket.
    """
    try:
        # Set a short timeout for receiving data
        s.settimeout(2)
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner
    except (socket.timeout, ConnectionResetError):
        return "Could not grab banner."
    except Exception as e:
        return f"Error grabbing banner: {e}"

def scan_port(target_host, port):
    """
    Scans a single port on the target host.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_host, port))
            if result == 0:
                banner = get_banner(s)
                with print_lock:
                    print(f"[+] Port {port:<5} is open   | Service: {banner}")
    except socket.gaierror:
        # This error happens if the hostname can't be resolved.
        # We only need to report it once, so we'll let the main thread handle it.
        pass
    except Exception as e:
        with print_lock:
            print(f"[-] Error scanning port {port}: {e}")

def worker(target_host, q):
    """
    The worker function for each thread.
    Pulls a port from the queue and scans it.
    """
    while not q.empty():
        port = q.get()
        scan_port(target_host, port)
        q.task_done()

def main():
    # --- 1. Argument Parsing ---
    parser = argparse.ArgumentParser(description="A simple, multi-threaded TCP port scanner.")
    parser.add_argument("target", help="The target host to scan (IP address or domain name).")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (e.g., 1-1024, 80, 443).")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads to use.")
    
    args = parser.parse_args()

    target = args.target
    num_threads = args.threads
    
    # --- 2. Port Parsing ---
    ports_to_scan = []
    try:
        if '-' in args.ports:
            start_port, end_port = map(int, args.ports.split('-'))
            ports_to_scan = range(start_port, end_port + 1)
        else:
            ports_to_scan = [int(p.strip()) for p in args.ports.split(',')]
    except ValueError:
        print("[-] Invalid port format. Use a range like '1-1024' or comma-separated ports like '80,443'.")
        sys.exit(1)

    # --- 3. Setup and Execution ---
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Using {num_threads} threads.")
    print("-" * 50)
    
    # Resolve hostname to IP address to avoid resolving it in every thread
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolved {target} to {target_ip}\n")
    except socket.gaierror:
        print(f"[-] Could not resolve hostname: {target}. Exiting.")
        sys.exit(1)

    # Create a queue and fill it with ports
    q = Queue()
    for port in ports_to_scan:
        q.put(port)
        
    # Create and start the worker threads
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(target_ip, q))
        thread.daemon = True  # Allows main thread to exit even if workers are blocking
        thread.start()
        
    # Wait for the queue to be empty
    q.join()
    
    print("\n" + "-" * 50)
    print("Scan complete.")
    print(f"Time finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

if __name__ == "__main__":
    main()