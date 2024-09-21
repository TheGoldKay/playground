import os
import sys
import time
import atexit
import signal
import logging

PID_FILE = '/tmp/mydaemon.pid'
LOG_FILE = '/tmp/mydaemon.log'

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def daemonize():
    """Daemonize the process."""
    # Perform first fork
    if os.fork() > 0:
        # Exit the parent process
        sys.exit()

    # Change the working directory
    os.chdir("/")
    # Set new file permissions
    os.umask(0)
    # Create a new session
    os.setsid()

    # Perform second fork
    if os.fork() > 0:
        # Exit the first child process
        sys.exit()

    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()
    with open(os.devnull, 'r') as devnull:
        os.dup2(devnull.fileno(), sys.stdin.fileno())
    with open(LOG_FILE, 'a+') as log_file:
        os.dup2(log_file.fileno(), sys.stdout.fileno())
        os.dup2(log_file.fileno(), sys.stderr.fileno())

    # Write the PID file
    with open(PID_FILE, 'w') as f:
        f.write(str(os.getpid()))

    # Register the exit function
    atexit.register(lambda: os.remove(PID_FILE))

def signal_handler(signum, frame):
    """Handle termination signals."""
    logging.info("Daemon received shutdown signal.")
    sys.exit()

def main():
    """Main loop of the daemon."""
    while True:
        logging.info("Daemon is running...")
        time.sleep(5)

def start():
    """Start the daemon."""
    if os.path.isfile(PID_FILE):
        print("Daemon is already running.")
        sys.exit(1)

    daemonize()
    main()

def stop():
    """Stop the daemon."""
    if not os.path.isfile(PID_FILE):
        print("Daemon is not running.")
        sys.exit(1)

    with open(PID_FILE, 'r') as f:
        pid = int(f.read().strip())

    os.kill(pid, signal.SIGTERM)
    os.remove(PID_FILE)
    logging.info("Daemon stopped.")

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    
    if len(sys.argv) != 2:
        print("Usage: {} start|stop".format(sys.argv[0]))
        sys.exit(1)

    if sys.argv[1] == 'start':
        start()
    elif sys.argv[1] == 'stop':
        stop()
    else:
        print("Invalid command. Use 'start' or 'stop'.")
        sys.exit(1)
