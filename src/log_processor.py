import json
from typing import Any
from confluent_kafka import KafkaException, KafkaError, Message
from concurrent.futures import ThreadPoolExecutor, Future
from src.kafka_consumer import KafkaConsumer
from src.loki_client import LokiClient

class LogProcessor:
    def __init__(self, kafka_consumer: KafkaConsumer, loki_client: LokiClient):
        self.kafka_consumer = kafka_consumer
        self.loki_client = loki_client
        self.executor = ThreadPoolExecutor(max_workers=10)
    
    def process_logs(self) -> None:
        self.kafka_consumer.subscribe()
        try:
            while True:
                msg: Message = self.kafka_consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print(f"End of partition {msg.partition()} for topic {msg.topic()} reached")
                    else:
                        raise KafkaException(msg.error())
                else:
                    log: Any = json.loads(msg.value().decode('utf-8'))
                    future: Future = self.executor.submit(self.loki_client.send_log, log)
                    future.add_done_callback(self.log_result)
        except KeyboardInterrupt:
            pass
        finally:
            self.kafka_consumer.close()

    @staticmethod
    def log_result(future: Future) -> None:
        if future.exception() is not None:
            print(f"Error in sending log: {future.exception()}")
