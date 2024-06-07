import json
import requests
from typing import Any, Dict

class LokiClient:
    def __init__(self, loki_url: str, job_name: str):
        self.loki_url = loki_url
        self.job_name = job_name
        self.headers = {'Content-Type': 'application/json'}
    
    def send_log(self, log: Dict[str, Any]) -> None:
        payload = {
            "streams": [
                {
                    "labels": f"{{job=\"{self.job_name}\"}}",
                    "entries": [
                        {"ts": log['timestamp'], "line": json.dumps(log)}
                    ]
                }
            ]
        }
        response = requests.post(self.loki_url, headers=self.headers, data=json.dumps(payload))
        if response.status_code != 204:
            print(f"Error in sending log data to Loki: {response.status_code}, {response.text}")
