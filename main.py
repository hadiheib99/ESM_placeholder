import random
import json

def generate_random_events():
    events = [{"event_id": i, "value": random.random()} for i in range(10)]

    return json.dumps(events)

if __name__ == "__main__":
    print("Generated Events:")
    print(generate_random_events() )
