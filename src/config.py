from dataclasses import dataclass

@dataclass
class KafkaConfig:
    bootstrap_servers: str
    group_id: str
    topic: str

@dataclass
class LokiConfig:
    url: str
    job_name: str

@dataclass
class Config:
    kafka: KafkaConfig
    loki: LokiConfig
