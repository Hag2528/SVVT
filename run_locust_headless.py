import subprocess
import time
import os
import sys

# Ensure output isn't buffered
sys.stdout.reconfigure(line_buffering=True)

# Set the environment variables
os.environ["LOCUST_HOST"] = "http://127.0.0.1:8000"
os.environ["LOCUST_USERS"] = "10"
os.environ["LOCUST_SPAWN_RATE"] = "1"
os.environ["LOCUST_RUN_TIME"] = "10s"

# Run Locust in headless mode
cmd = [
    "locust", 
    "-f", "locustfile.py", 
    "--headless", 
    "--host", os.environ["LOCUST_HOST"],
    "--users", os.environ["LOCUST_USERS"],
    "--spawn-rate", os.environ["LOCUST_SPAWN_RATE"],
    "--run-time", os.environ["LOCUST_RUN_TIME"],
    "--csv=locust_results"
]

print("Starting Locust in headless mode...")
print(f"Command: {' '.join(cmd)}")

try:
    # Use subprocess.run instead of Popen for simpler handling
    process = subprocess.run(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True,
        bufsize=1,  # Line buffered
        check=True
    )
    
    # Print output
    print("STDOUT:")
    print(process.stdout)
    
    # Print any errors
    if process.stderr:
        print("STDERR:")
        print(process.stderr)
    
    print("Locust test completed!")
    print("Results saved to locust_results_stats.csv, locust_results_failures.csv, and locust_results_history.csv")
    
except subprocess.CalledProcessError as e:
    print(f"Error running Locust (exit code {e.returncode}):")
    print(f"STDOUT: {e.stdout}")
    print(f"STDERR: {e.stderr}")
except Exception as e:
    print(f"Error running Locust: {e}")




