from kafka import KafkaConsumer
import time
topic = 'mlpredictive'
consumer = KafkaConsumer(topic,
     bootstrap_servers='localhost:29092',
     group_id ="bigdata",
     max_poll_records =1, 
     auto_offset_reset='earliest',
     enable_auto_commit=True)
print("Listo para recibir en mlpredictive")
for msg in consumer:
    print (msg)
    time.sleep(0.1)