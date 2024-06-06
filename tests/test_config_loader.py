import unittest
from src.config_loader import ConfigLoader
from src.config import Config, KafkaConfig, LokiConfig

class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config_loader = ConfigLoader('tests/test_config.yaml')
        config = config_loader.config

        expected_kafka_config = KafkaConfig(bootstrap_servers='localhost:9092', group_id='test_group', topic='test_topic')
        expected_loki_config = LokiConfig(url='http://test_loki_server/loki/api/v1/push', job_name='test_job')
        expected_config = Config(expected_kafka_config, expected_loki_config)
        
        self.assertEqual(config.kafka.bootstrap_servers, expected_kafka_config.bootstrap_servers)
        self.assertEqual(config.kafka.group_id, expected_kafka_config.group_id)
        self.assertEqual(config.kafka.topic, expected_kafka_config.topic)
        
        self.assertEqual(config.loki.url, expected_loki_config.url)
        self.assertEqual(config.loki.job_name, expected_loki_config.job_name)

if __name__ == '__main__':
    unittest.main()
