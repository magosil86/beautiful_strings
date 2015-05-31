def clean_string(input):
	input = input.lower()
	letters = [char for char in input if char.isalpha()]
	cleaned = "".join(letters)
	return cleaned

def count_chars(input):
	input = clean_string(input)
	counts = {}
	for char in input:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	return counts

def assign_values(input):
	counts = count_chars(input)
	sorted_chars = sorted(counts, key=counts.get, reverse=True)
	values = {}
	beauty = 26
	for char in sorted_chars:
		values[char] = beauty
		beauty = beauty - 1
	return values

def calculate_beauty(input):
	input = clean_string(input)
	values = assign_values(input)
	total = 0
	for char in input:
		if char.isalpha():
			total += values[char]
	return total