# write function tests here, don't add input('') statements here!
import unittest
from question_c.question_c import get_most_likely_ancestor_consensus

# follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import test_config

class TestConfig(unittest.TestCase):

    def test_question_c_config(self):
        self.assertEqual(True, test_config())

    def test_question_c(self):
        positions = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        x, y, z = positions  # Corrected this line
        x = positions[0]
        y = positions[1]
        z = positions[2]
        self.assertEqual(x, 2)
        print(x)
        self.assertEqual(y, 4)
        print(y)
        self.assertEqual(z, 10)
        print(z)
        self.assertEqual(positions, (2, 4, 10))
        print(positions)
    


