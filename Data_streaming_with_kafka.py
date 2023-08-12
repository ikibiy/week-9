# -*- coding: utf-8 -*-
"""Week9-Data Streaming with Kafka

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSFyD94aG-0wvsRRD6ieJhd-2693au2b
"""

-*- coding: utf-8 -*-
"""Data Streaming with Kafka Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LQg8YAFt4d9zHhzgXOjjA8cZL8yIy0Mc
"""

!pip install confluent-kafka #install confluent-kafka

from confluent_kafka import Producer, Consumer, KafkaError
import json

# Set up Confluent Cloud credentials for producer
conf = {
'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
'security.protocol': 'SASL_SSL',
'sasl.mechanism': 'PLAIN',
'sasl.username': 'PBLZTYNSYXUNEDWJ',
'sasl.password': 'TFVC+XYaBB9b2WkCBF8OnzrzNpA+MHtg/r/PJhMq9aX6wJR7hGHJavGPVIx8QEqK', 
'group.id': 'cluster_0',
'auto.offset.reset': 'earliest'
}


# Create a Kafka producer instance
producer = Producer(conf)
# Publish data to the topic every second
topic_name = 'topic_0'

data = {"transaction_id": "12345",
        "sender_phone_number": "256777123456",
        "receiver_phone_number": "256772987654",
        "transaction_amount": 100000,
        "transaction_time": "2023-04-19 12:00:00"}

message = json.dumps(data).encode('utf-8')

producer.produce(topic_name, message)
producer.flush()

print(f"Published message '{message}' to topic '{topic_name}'")


# Create a Kafka producer instance
consumer = Consumer(conf)
topic_name = 'topic_0'

# Subscribe to your Confluent Cloud topic and consume messages
consumer.subscribe([topic_name])
while True:
  msg = consumer.poll(1.0)
  if msg is None:
    break
  if msg.error():
    print("Consumer error: {}".format(msg.error()))
    continue
  print('Received message: {}'.format(msg.value().decode('utf-8')))