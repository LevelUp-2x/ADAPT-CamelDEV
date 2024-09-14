import unittest
from unittest.mock import patch, MagicMock
from ADAPT-CamelDEV-Project.langchain_integration.rag_service import app

class TestRAGService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.vector_store')
    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.qa_chain')
    def test_query_route(self, mock_qa_chain, mock_vector_store):
        mock_qa_chain.return_value = {
            'result': 'Test answer',
            'source_documents': [MagicMock(page_content='Test content', metadata={'source': 'Test source'})]
        }

        test_query = {"query": "Test query"}
        response = self.app.post('/query',
                                 json=test_query,
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('answer', data)
        self.assertIn('source_documents', data)
        self.assertEqual(data['answer'], 'Test answer')
        self.assertEqual(len(data['source_documents']), 1)
        self.assertEqual(data['source_documents'][0]['content'], 'Test content')
        self.assertEqual(data['source_documents'][0]['metadata']['source'], 'Test source')

    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.vector_store')
    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.CharacterTextSplitter')
    def test_ingest_route(self, mock_text_splitter, mock_vector_store):
        mock_text_splitter.return_value.split_text.return_value = ['chunk1', 'chunk2']
        mock_vector_store.add_texts.return_value = ['doc1', 'doc2']

        test_document = {"document": "Test document content"}
        response = self.app.post('/ingest',
                                 json=test_document,
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertIn('2', data['message'])
        mock_text_splitter.return_value.split_text.assert_called_once_with("Test document content")
        mock_vector_store.add_texts.assert_called_once_with(['chunk1', 'chunk2'])

    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.vector_store')
    @patch('ADAPT-CamelDEV-Project.langchain_integration.rag_service.qa_chain')
    def test_query_route_error(self, mock_qa_chain, mock_vector_store):
        mock_qa_chain.side_effect = Exception("Test error")

        test_query = {"query": "Test query"}
        response = self.app.post('/query',
                                 json=test_query,
                                 content_type='application/json')

        self.assertEqual(response.status_code, 500)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], "An error occurred while processing your query")

if __name__ == '__main__':
    unittest.main()