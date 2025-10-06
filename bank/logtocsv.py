import csv

with open("logs/app.log", "r") as infile, open("logs/app.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Timestamp", "Level", "Message"])
    for line in infile:
        parts = line.strip().split(",", 2)
        if len(parts) == 3:
            writer.writerow(parts)
