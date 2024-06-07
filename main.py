from src.config_loader import ConfigLoader
from src.kafka_consumer import KafkaConsumer
from src.loki_client import LokiClient
from src.log_processor import LogProcessor

if __name__ == '__main__':
    config_loader = ConfigLoader('config.yaml')
    kafka_consumer = KafkaConsumer(config_loader.config)
    loki_client = LokiClient('http://your_loki_server/loki/api/v1/push', 'your_job_name')
    log_processor = LogProcessor(kafka_consumer, loki_client)
    
    log_processor.process_logs()
