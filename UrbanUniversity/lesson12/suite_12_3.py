import unittest

import test_12_1
import test_12_2


test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
