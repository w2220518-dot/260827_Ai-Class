import json
import time
from datetime import datetime
from urllib.error import URLError
from urllib.request import urlopen


API_URL = "https://api.exchangerate-api.com/v4/latest/{currency}"
SUPPORTED_CURRENCIES = {
	"1": ("USD", "미국 달러"),
	"2": ("JPY", "일본 엔"),
	"3": ("CNY", "중국 위안"),
}
REFRESH_INTERVAL = 30


def get_exchange_rate(currency):
	"""선택한 통화의 최신 원화 환율을 가져옵니다."""
	url = API_URL.format(currency=currency)

	with urlopen(url, timeout=10) as response:
		data = json.load(response)

	return data["rates"]["KRW"]


def clear_screen():
	print("\033[2J\033[H", end="")


def display_exchange_rate(currency, currency_name, rate):
	clear_screen()
	updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print("=== 실시간 환율 정보 ===")
	print(f"통화: {currency_name} ({currency})")
	print(f"1 {currency} = {rate:,.2f} KRW")
	print(f"업데이트: {updated_at}")
	print(f"\n{REFRESH_INTERVAL}초 후에 자동으로 갱신됩니다. 종료하려면 Ctrl+C를 누르세요.")


def choose_currency():
	print("환율을 조회할 통화를 선택하세요.")
	for number, (_, name) in SUPPORTED_CURRENCIES.items():
		print(f"{number}. {name}")

	while True:
		choice = input("선택 (1~3): ").strip()
		if choice in SUPPORTED_CURRENCIES:
			return SUPPORTED_CURRENCIES[choice]
		print("1, 2, 3 중 하나를 입력해 주세요.")


def run():
	currency, currency_name = choose_currency()

	try:
		while True:
			try:
				rate = get_exchange_rate(currency)
				display_exchange_rate(currency, currency_name, rate)
			except (KeyError, TypeError, URLError, TimeoutError, ValueError) as error:
				clear_screen()
				print("환율 정보를 가져오지 못했습니다.")
				print(f"잠시 후 다시 시도합니다. ({error})")

			time.sleep(REFRESH_INTERVAL)
	except KeyboardInterrupt:
		print("\n환율 조회를 종료합니다.")


if __name__ == "__main__":
	run()
