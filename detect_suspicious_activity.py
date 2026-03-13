import re

log_file = "sample_logs.txt"

suspicious_patterns = [
    "powershell",
    "wget",
    "curl",
    "nc",
    "whoami"
]

def analyze_logs():
    try:
        with open(log_file, "r") as file:
            logs = file.readlines()

        for line in logs:
            for pattern in suspicious_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    print("[ALERT] Suspicious activity detected:", 
line.strip())

    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    analyze_logs()
