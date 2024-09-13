import unittest
from unittest.mock import patch, MagicMock
from ADAPT_CamelDEV_Project.langchain_integration.basic_agent import agent_executor, AgentHierarchy

class TestBasicAgent(unittest.TestCase):
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.search_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.calculator_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.image_analysis_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.ethics_check_tool')
    def test_agent_weather_query(self, mock_ethics, mock_image, mock_calculator, mock_search):
        mock_search.return_value = "The weather in New York is sunny with a high of 75°F."
        mock_calculator.return_value = 0  # Not used in this test
        mock_image.return_value = ""  # Not used in this test
        mock_ethics.return_value = True

        result = agent_executor.run("What is the weather like in New York?")
        
        self.assertIn("sunny", result.lower())
        self.assertIn("75", result)
        mock_search.assert_called_once()
        mock_calculator.assert_not_called()
        mock_image.assert_not_called()
        mock_ethics.assert_called()  # Ethics check should be called for any action

    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.search_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.calculator_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.image_analysis_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.ethics_check_tool')
    def test_agent_calculation(self, mock_ethics, mock_image, mock_calculator, mock_search):
        mock_calculator.return_value = 15
        mock_search.return_value = ""  # Not used in this test
        mock_image.return_value = ""  # Not used in this test
        mock_ethics.return_value = True

        result = agent_executor.run("What is 5 + 10?")
        
        self.assertIn("15", result)
        mock_calculator.assert_called_once()
        mock_search.assert_not_called()
        mock_image.assert_not_called()
        mock_ethics.assert_called()  # Ethics check should be called for any action

    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.search_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.calculator_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.image_analysis_tool')
    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.ethics_check_tool')
    def test_agent_image_analysis(self, mock_ethics, mock_image, mock_calculator, mock_search):
        mock_image.return_value = "The image shows the NYC skyline with tall skyscrapers."
        mock_search.return_value = "The weather in New York is cloudy."
        mock_calculator.return_value = 0  # Not used in this test
        mock_ethics.return_value = True

        result = agent_executor.run("What is the weather like in New York? Also, analyze this image of the NYC skyline: nyc_skyline.jpg")
        
        self.assertIn("cloudy", result.lower())
        self.assertIn("skyline", result.lower())
        self.assertIn("skyscrapers", result.lower())
        mock_search.assert_called_once()
        mock_image.assert_called_once()
        mock_calculator.assert_not_called()
        mock_ethics.assert_called()  # Ethics check should be called for any action

    def test_agent_hierarchy(self):
        mock_agent = MagicMock()
        hierarchy = AgentHierarchy([mock_agent])
        
        task = "Test task"
        hierarchy.assign_task(task)
        
        # Check if the mock agent was called with the task
        mock_agent.run.assert_called_once_with(task)

    @patch('ADAPT_CamelDEV_Project.langchain_integration.basic_agent.ethics_check_tool')
    def test_ethics_check(self, mock_ethics):
        mock_ethics.return_value = False

        with self.assertRaises(Exception):
            agent_executor.run("Perform an unethical action")

        mock_ethics.assert_called_once()

if __name__ == '__main__':
    unittest.main()