import subprocess
import sys

print("Starting Locust with web interface...")

# Run Locust with web interface
cmd = [
    "locust",
    "-f", "locustfile.py",
    "--host", "http://127.0.0.1:8000"  # Your Django server
]

print(f"Command: {' '.join(cmd)}")
print("Open http://localhost:8089 in your browser to access the Locust web interface")
print("Then enter the number of users and spawn rate to start the test")

try:
    # Use subprocess.run to keep the process running
    process = subprocess.run(
        cmd,
        check=True
    )
    
    print("Locust process ended")
    
except subprocess.CalledProcessError as e:
    print(f"Error running Locust (exit code {e.returncode})")
except Exception as e:
    print(f"Error running Locust: {e}")
except KeyboardInterrupt:
    print("Locust stopped by user")