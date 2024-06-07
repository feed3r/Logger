from typing import Any, Dict
from confluent_kafka import Consumer, KafkaException, KafkaError, Message
from src.config import KafkaConfig

class KafkaConsumer:
    def __init__(self, config: KafkaConfig):
        self.consumer = Consumer({
            'bootstrap.servers': config.bootstrap_servers,
            'group.id': config.group_id,
            'auto.offset.reset': 'earliest'
        })
        self.topic = config.topic
    
    def subscribe(self) -> None:
        self.consumer.subscribe([self.topic])

    def poll(self, timeout: float) -> Message:
        return self.consumer.poll(timeout)
    
    def close(self) -> None:
        self.consumer.close()
