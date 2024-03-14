import random

def main():
	print("***********************  1A2B  ***********************")
	ans = generate_ans()
	while True:
		g = input("please guess the non-repeated four-digit number:")
		if check_input(g) == False:
			print("!!!PLEASE ENTER NON-REPEAT 4-DIGIT NUMBER!!!")
			continue
		guess = create_guess(g)
		if guess == ans:
			print("right guess!")
			break
		else:
			check(guess, ans)


def check(guess, ans):
	a = 0
	b = 0
	for x in ans:
		if x in guess:
			if ans.index(x) == guess.index(x):
				a += 1
			elif ans.index(x) != guess.index(x):
				b += 1
	print("A:", a, " B:", b)


def generate_ans():
	ans = random.sample(range(10), 4)
	# print(ans)
	return ans


def create_guess(g):
	guess = []
	guess.extend([int(g[0]), int(g[1]), int(g[2]), int(g[3])])
	print(guess)
	return guess


def check_input(g):
	if not g.isdigit():
		return False
	if len(g) != 4:
		return False

	seen_digits = set()
	for digit in g:
		if digit in seen_digits:
			return False
		seen_digits.add(digit)
	return True

main()




