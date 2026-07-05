import re
with open("sample2.txt", "w") as file:
    file.write ("8:30 PM 06/27/2026 LOGIN_FAILED 192.168.1.5 \n")
    file.write ("8:45 PM 06/27/2026 LOGIN_FAILED 192.168.1.5\n")
    file.write ("8:50 PM 06/27/2026 LOGIN_SUCCESSED 192.168.1.5\n")
print("Log Created")
with open("sample2.txt" , "r") as file:
    logs = file.readlines()
    print("Contents of the log file") #indented
for log in logs:
     print(log.strip())

for log in logs:
    pattern = pattern = pattern = r"(\d{1,2}:\d{2}\s+[AP]M\s+\d{2}/\d{2}/\d{4})\s+(\w+)\s+([\d.]+)"
    #r"(\d{1,2}:\d{2}\s+\w+\s+\d{2}/\d{2}/\d{4})\s+(LOGIN_\w+)\s+([\d.]+)"
    
    match = re.search(pattern, log)

    if match:
        timestamp = match.group(1)
        event = match.group(2)
        ip = match.group(3)

        print(f"Timestamp: {timestamp}")
        print(f"Event: {event}")
        print(f"IP Address: {ip}")
        print("_" * 30)