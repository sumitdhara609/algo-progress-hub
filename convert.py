import json

data = []

with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")

        if len(parts) < 6:
            continue

        name, difficulty, topic, pattern, status, link = parts

        data.append({
            "name": name,
            "difficulty": difficulty,
            "topic": topic,
            "pattern": pattern,
            "status": status,
            "link": link
        })

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ Data converted successfully!")