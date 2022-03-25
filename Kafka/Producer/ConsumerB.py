from tokenize import group
from kafka import KafkaConsumer
import time
topic = 'stefania'
consumer = KafkaConsumer(topic,
    client_id='B',
     bootstrap_servers='localhost:29092',
     group_id ="bigdata",
     max_poll_records =1, 
     auto_offset_reset='earliest',
     enable_auto_commit=True)

print("Listo para recibir en mlpredictive consumer B")
for msg in consumer:
    time.sleep(1)
    print (msg)