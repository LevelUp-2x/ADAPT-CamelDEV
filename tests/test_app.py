import unittest
from ADAPT-CamelDEV-Project.langchain_integration.app import app
import json

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ADAPT-CamelDEV', response.data)

    def test_multi_agent_chat_route(self):
        test_message = {"message": "Test message"}
        response = self.app.post('/multi_agent_chat',
                                 data=json.dumps(test_message),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('responses', data)
        self.assertIsInstance(data['responses'], list)
        self.assertTrue(len(data['responses']) > 0)

    def test_query_route(self):
        test_query = {"query": "What is ADAPT-CamelDEV?"}
        response = self.app.post('/query',
                                 data=json.dumps(test_query),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('rag_answer', data)
        self.assertIn('graph_rag_answer', data)

    def test_ingest_route(self):
        test_document = {"document": "This is a test document for ADAPT-CamelDEV."}
        response = self.app.post('/ingest',
                                 data=json.dumps(test_document),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('rag_ingest_status', data)
        self.assertIn('graph_rag_ingest_status', data)

    def test_get_memory_route(self):
        response = self.app.get('/get_memory')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('short_term_memory', data)
        self.assertIn('long_term_memory', data)

    def test_clear_memory_route(self):
        response = self.app.post('/clear_memory')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Memory cleared successfully')

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()