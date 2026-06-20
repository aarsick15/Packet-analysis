import re
with open("sample_logs.txt", "w") as file:
    file.write("2026-08-10 08:15:22 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:15:25 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:15:30 LOGIN_SUCCESS 192.168.1.60\n")
print("Log file created!")
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()
print("\nContents of the log file:")
for log in logs:
    print(log.strip())
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    pattern = "(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(LOGIN_\w+)\s+([\d.]+)"
    match = re.search(pattern, log)

    if match:
        timestamp = match.group(1)
        event = match.group(2)
        ip = match.group(3)

        print(f"Timestamp: {timestamp}")
        print(f"Event:{event}")
        print(f"IP Address: {ip}")
        print("_" * 30)
