import yaml
from typing import Any, Dict
from src.config import Config, KafkaConfig, LokiConfig

class ConfigLoader:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
    
    @staticmethod
    def load_config(config_file: str) -> Config:
        with open(config_file, 'r') as file:
            config_data: Any = yaml.safe_load(file)
            kafka_config = KafkaConfig(**config_data['kafka'])
            loki_config = LokiConfig(**config_data['loki'])
            return Config(kafka_config, loki_config)
