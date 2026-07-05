import re

with open("sample_logs.txt", "w") as file:
    file.write("2026-08-10 08:15:22 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:15:25 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:20:30 LOGIN_SUCCESS 192.168.1.60\n")
    file.write("2026-08-10 08:25:30 LOGIN_SUCCESS 192.168.1.60\n")
    file.write("2026-08-10 08:25:50 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:27:37 LOGIN_SUCCESS 192.168.1.60\n")
    file.write("2026-08-10 08:30:36 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:35:34 LOGIN_FAILED 192.168.1.50\n")
    file.write("2026-08-10 08:37:34 LOGIN_SUCCESS 192.168.1.60\n")
    file.write("2026-08-10 08:47:30 LOGIN_SUCCESS 192.168.1.60\n")
print("Log file created!")
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()
print("\nContents of the log file:")
for log in logs:
    print(log.strip())
failed_ips = {}
success_ips = {}
for log in logs:
    pattern = "(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (LOGIN_\w+)\s+([\d.]+)"
    match = re.search(pattern, log)
    
    if match:
        timestamp = match.group(1)
        event = match.group(2)
        ip = match.group(3)

        print(f"Timestamp: {timestamp}")
        print(f"Event: {event}")
        print(f"IP Address: {ip}")
        print("_" * 30)

    if event == "LOGIN_FAILED":  
            failed_ips[ip] = failed_ips.get(ip, 0)+1
    elif event == "LOGIN_SUCCESS":  
            success_ips[ip] = success_ips.get(ip, 0)+1 
print("\nResults:")       
for ip, count in failed_ips.items():
    print(f"{ip}: {count} Failed attempts")
    
for ip, count in success_ips.items():
    print(f"{ip}: {count} Successful attempts")
    print("_" * 10)
print("\nChecking for suspicious IPs")
print("=" * 30)

for ip, count in failed_ips.items():
    if count >=5:
        print(f"🚨😭🚨 Alert! : {ip} is suspicious!")
        print(f"Reason : {count} failed attempts.")
        print( "_" * 5)

    elif count >= 3:
        print(f"⚠️ WARNING: {ip}")
        print(f"Reason: {count} Failed attempts")



# Total_ips = len(failed_ips) + len(success_ips)
# print("\n",Total_ips) #total number of unique ip logs

# Total_number_failed = sum(failed_ips.values())
# print("\n",Total_number_failed)

# Total_number_success = sum(success_ips.values())
# print("\n", Total_number_success)

# Number_unique_failed = len(failed_ips)
# print("\n",Number_unique_failed, sep="")

# Number_unique_success = len(success_ips)
# print(Number_unique_success)

import csv
with open("security_report.csv", "w", newline = "") as file:
     writer = csv.writer(file)

     writer.writerow([
          "IP Address",
          "Failed Attempts",
          "Successful Attempts",
          "Status",
        
     ])

     all_ips = set(failed_ips.keys()) | set(success_ips.keys())

     for ip in all_ips:
          failed = failed_ips.get(ip, 0)
          success = success_ips.get(ip, 0)

          if failed >= 5:
               status = "SUSPICIOUS"
          else:
               status = "NORMAL"
          writer.writerow([
               ip,
               failed,
               success,
               status
          ])
print("security_report.csv created successfully!")