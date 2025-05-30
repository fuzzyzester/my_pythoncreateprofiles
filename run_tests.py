import unittest

# Discover and run all tests in the current directory
loader = unittest.TestLoader()
suite = loader.discover('.')

runner = unittest.TextTestRunner()
runner.run(suite)
