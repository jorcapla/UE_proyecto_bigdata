from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time
import random
import hashlib

def hash_partitioner(key, all_partitions, available):
    """
    Customer Kafka partitioner to get the partition corresponding to key
    :param key: partitioning key
    :param all_partitions: list of all partitions sorted by partition ID
    :param available: list of available partitions in no particular order
    :return: one of the values from all_partitions or available
    """

    if key is None:
        if available:
            return random.randint(0, 2)
        return random.randint(0, 2)

    idx = int(hashlib.sha1(key).hexdigest(), 16) % (10 ** 8)
    idx &= 0x7fffffff
    idx %= len(all_partitions)
    return all_partitions[idx]

#creo topic
from kafka import KafkaAdminClient
from kafka.admin import NewPartitions

topic = 'mlpredictive'
topic_device='mlpredictive'
bootstrap_servers = 'localhost:29092'

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_partitions = {}
topic_partitions[topic_device] = NewPartitions(total_count=3)
#admin_client.create_partitions(topic_partitions)


# produzco 
producer = KafkaProducer(bootstrap_servers=['localhost:29092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Asynchronous by default
for _ in range(100):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive01','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
time.sleep(1)
for _ in range(100):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive02','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
time.sleep(1)
for _ in range(100):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive03','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
time.sleep(1)
for _ in range(100):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive04','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
time.sleep(1)
for _ in range(100):
    future = producer.send(topic=topic_device, value ={'device':'mlpredictive05','temperature': '25.0'})
    result = future.get(timeout=30)
    print(result)
time.sleep(1)