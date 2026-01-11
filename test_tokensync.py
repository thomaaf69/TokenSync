# test_tokensync.py
"""
Tests for TokenSync module.
"""

import unittest
from tokensync import TokenSync

class TestTokenSync(unittest.TestCase):
    """Test cases for TokenSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenSync()
        self.assertIsInstance(instance, TokenSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
