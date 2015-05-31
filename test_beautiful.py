import unittest
from beautiful import count_chars, assign_values, calculate_beauty

class TestBeautifulStrings(unittest.TestCase):

	def test_count_chars_in_string(self):
		test_string = "aabcdee"
		expected_counts = {
			'a': 2,
			'b':1, 
			'c': 1,
			'd':1,
			'e': 2
		}
		counts = count_chars(test_string)
		self.assertEqual(expected_counts, counts)

	def test_count_chars_ignores_spaces(self):
		test_string = "aa bb"
		expected_counts = {
			'a':2,
			'b':2
		}
		counts = count_chars(test_string)
		self.assertEqual(expected_counts, counts)

	def test_count_chars_ignores_punctuation(self):
		test_string = ":) happy"
		expected_counts = {
			'h': 1,
			'a': 1,
			'p': 2,
			'y': 1
		}
		counts = count_chars(test_string)
		self.assertEqual(expected_counts, counts)

	def test_assign_value(self):
		test_string="aaabbbbcccccdee"
		expected_counts = {
			'a': 24,
			'b': 25,
			'c': 26, 
			'd': 22,
			'e': 23
		}
		counts = assign_values(test_string)
		self.assertEqual(expected_counts, counts)

	def test_calculate_beauty(self):
		test_string = "ABbCcc"
		test_string2 = "So I just go consult Professor Dalves"
		expected_beauty = 152
		expected_beauty2 = 646
		beauty = calculate_beauty(test_string)
		beauty2 = calculate_beauty(test_string2)
		self.assertEqual(expected_beauty, beauty)
		self.assertEqual(expected_beauty2, beauty2)

if __name__ == "__main__":
	unittest.main()