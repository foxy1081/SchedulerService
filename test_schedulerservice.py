# test_schedulerservice.py
"""
Tests for SchedulerService module.
"""

import unittest
from schedulerservice import SchedulerService

class TestSchedulerService(unittest.TestCase):
    """Test cases for SchedulerService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SchedulerService()
        self.assertIsInstance(instance, SchedulerService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SchedulerService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
