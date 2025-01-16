from confluent_kafka import Producer
import random
import time

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Update with your Kafka broker address
}
producer = Producer(producer_config)

# Callback for delivery report
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record successfully produced to {msg.topic()} partition {msg.partition()}")

# Event generator function
def generate_random_events():
    events = [
        {"event_id": i, "event_type": f"type_{random.randint(1, 5)}", "value": random.random()}
        for i in range(10)
    ]
    return events

# Send events to Kafka
def send_events_to_kafka(topic):
    events = generate_random_events()
    for event in events:
        producer.produce(
            topic=topic,
            key=str(event["event_id"]),
            value=str(event),
            callback=delivery_report
        )
        # Flush messages to Kafka to ensure delivery
        producer.flush()

if __name__ == "__main__":
    topic_name = "EPT_TOPIC"  # Replace with your Kafka topic name
    while True:
        send_events_to_kafka(topic_name)
        time.sleep(5)  # Wait for 5 seconds before generating the next batch
