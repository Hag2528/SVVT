import unittest
import sys
import inspect
import os
import datetime
from selenium_tests import ContractRenewalSystemTest

# Try to import xmlrunner, install if not available
try:
    import xmlrunner
except ImportError:
    print("xmlrunner not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "unittest-xml-reporting"])
    import xmlrunner

def list_available_tests():
    """List all available test methods in the ContractRenewalSystemTest class"""
    print("Available tests:")
    for name, method in inspect.getmembers(ContractRenewalSystemTest, predicate=inspect.isfunction):
        if name.startswith('test_'):
            print(f"  - {name}")

def run_all_tests(xml_report=False):
    """Run all tests in the ContractRenewalSystemTest class"""
    if xml_report:
        # Create reports directory if it doesn't exist
        if not os.path.exists('test_reports'):
            os.makedirs('test_reports')
        
        # Generate timestamp for report filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = f"test_reports/selenium_test_report_{timestamp}"
        
        runner = xmlrunner.XMLTestRunner(output=report_dir)
        suite = unittest.TestLoader().loadTestsFromTestCase(ContractRenewalSystemTest)
        runner.run(suite)
        print(f"XML report generated in: {report_dir}")
    else:
        unittest.main(module='selenium_tests')

def run_specific_test(test_name, xml_report=False):
    """Run a specific test by name"""
    suite = unittest.TestSuite()
    suite.addTest(ContractRenewalSystemTest(test_name))
    
    if xml_report:
        # Create reports directory if it doesn't exist
        if not os.path.exists('test_reports'):
            os.makedirs('test_reports')
        
        # Generate timestamp for report filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = f"test_reports/{test_name}_{timestamp}"
        
        runner = xmlrunner.XMLTestRunner(output=report_dir)
        runner.run(suite)
        print(f"XML report generated in: {report_dir}")
    else:
        runner = unittest.TextTestRunner()
        runner.run(suite)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python run_selenium_tests.py all            # Run all tests")
        print("  python run_selenium_tests.py all --xml      # Run all tests with XML report")
        print("  python run_selenium_tests.py list           # List available tests")
        print("  python run_selenium_tests.py test_name      # Run a specific test")
        print("  python run_selenium_tests.py test_name --xml  # Run a specific test with XML report")
        sys.exit(1)
    
    command = sys.argv[1]
    xml_report = "--xml" in sys.argv
    
    if command == "all":
        run_all_tests(xml_report)
    elif command == "list":
        list_available_tests()
    else:
        # Check if the test exists
        test_exists = False
        for name, method in inspect.getmembers(ContractRenewalSystemTest, predicate=inspect.isfunction):
            if name == command and name.startswith('test_'):
                test_exists = True
                break
        
        if test_exists:
            run_specific_test(command, xml_report)
        else:
            print(f"Error: Test '{command}' not found.")
            list_available_tests()
            sys.exit(1)


















