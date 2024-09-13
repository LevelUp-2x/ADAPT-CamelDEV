import unittest
import os
import sys

def run_tests():
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add the project root to the Python path
    project_root = os.path.abspath(os.path.join(current_dir))
    sys.path.insert(0, project_root)

    # Discover and run tests
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir=current_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    return result

if __name__ == '__main__':
    result = run_tests()
    if result.wasSuccessful():
        print("All tests passed successfully!")
        sys.exit(0)
    else:
        print("Some tests failed.")
        sys.exit(1)