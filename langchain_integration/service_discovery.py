import redis
import json
import time
from config import get_config

class ServiceDiscovery:
    def __init__(self):
        self.redis = redis.Redis(
            host=get_config('REDIS_HOST'),
            port=get_config('REDIS_PORT'),
            db=0
        )
        self.ttl = 30  # Time to live for service entries (in seconds)

    def register_service(self, service_name, host, port):
        service_info = json.dumps({
            'host': host,
            'port': port,
            'last_heartbeat': time.time()
        })
        self.redis.setex(f"service:{service_name}", self.ttl, service_info)

    def get_service(self, service_name):
        service_info = self.redis.get(f"service:{service_name}")
        if service_info:
            return json.loads(service_info)
        return None

    def heartbeat(self, service_name, host, port):
        self.register_service(service_name, host, port)

    def deregister_service(self, service_name):
        self.redis.delete(f"service:{service_name}")

    def list_services(self):
        services = {}
        for key in self.redis.scan_iter("service:*"):
            service_name = key.decode('utf-8').split(':')[1]
            service_info = self.get_service(service_name)
            if service_info:
                services[service_name] = service_info
        return services

# Usage example:
# sd = ServiceDiscovery()
# sd.register_service('rag_service', 'localhost', get_config('RAG_SERVICE_PORT'))
# service = sd.get_service('rag_service')
# print(service)  # {'host': 'localhost', 'port': 8001, 'last_heartbeat': 1234567890.123}
# services = sd.list_services()
# print(services)  # {'rag_service': {'host': 'localhost', 'port': 8001, 'last_heartbeat': 1234567890.123}}