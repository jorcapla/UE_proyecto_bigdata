from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import random
import hashlib


topic_device='mlpredictive'
kafka_servers = 'localhost:29092'

# produzco y envio mensaje
producer = KafkaProducer(bootstrap_servers=kafka_servers,value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for _ in range(1000):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive01','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
    #time.sleep(1)
# Asynchronous by default
