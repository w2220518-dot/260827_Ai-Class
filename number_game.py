import random


def play_game():
	target_number = random.randint(1, 100)
	attempts = 0

	print("1부터 100 사이의 숫자를 맞혀 보세요!")

	while True:
		try:
			guess = int(input("숫자를 입력하세요: "))
		except ValueError:
			print("숫자만 입력해 주세요.")
			continue

		if not 1 <= guess <= 100:
			print("1부터 100 사이의 숫자를 입력해 주세요.")
			continue

		attempts += 1

		if guess < target_number:
			print("더 큰 숫자입니다.")
		elif guess > target_number:
			print("더 작은 숫자입니다.")
		else:
			print(f"정답입니다! {attempts}번 만에 맞혔어요.")
			break


if __name__ == "__main__":
	play_game()
