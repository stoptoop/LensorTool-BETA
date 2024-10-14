import requests
from .config import *



def tokenopen():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	try:
		os.system('cls||clear')
		banner()
		print(f"{purple}>>>{end}   This option not work stable")
		token=input(f"{now_time()}~ Insert Token ~ {purple}[ {end}> {purple}]  {end}")

		print(f"""
	1 -> Chrome {purple}[{end} Windows / Linux {purple}]{end}
	2 -> Edge {purple}[{end} Windows {purple}]{end}
	3 -> Firefox {purple}[{end} Windows {purple}]{end}
		""")
		browser = input(f"{now_time()}~ Browser ~ {purple}[ {end}> {purple}]  {end}")

		if browser in ['1', '01']:
			try:
				navigator = "Chrome"
				print(colored_green(f"{navigator}  Starting.."))
				driver = webdriver.Chrome()
				print(colored_green(f"{navigator}  Ready"))
			except:
				print(colored_red_purple(f"{navigator}  Not installed or driver not up to date."))

		elif browser in ['2', '02']:
			if sys.platform.startswith("linux"):
				print("error")
			else:
				try:
					navigator = "Edge"
					print(colored_green(f"{navigator}  Starting.."))
					driver = webdriver.Edge()
					print(colored_green(f"{navigator}  Ready"))
				except:
					print(colored_red_purple(f"{navigator}  Not installed or driver not up to date."))


		elif browser in ['3', '03']:
			if sys.platform.startswith("linux"):
				print("error")
			else:
				try:
					navigator = "Firefox"
					print(colored_green(f"{navigator}  Starting.."))
					driver = webdriver.Firefox()
					print(colored_green(f"{navigator}  Ready"))
				except:
					print(colored_red_purple(f"{navigator}  Not installed or driver not up to date."))

		else:
			print("error")
		
		try:
			script = """
					function login(token) {
					setInterval(() => {
					document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
					}, 50);
					setTimeout(() => {
					location.reload();
					}, 2500);
					}
					"""
			driver.get("https://discord.com/login")
			print(f"{now_time()}", colored_green(f"Token Connection.. "))
			driver.execute_script(script + f'\nlogin("{token}")')
			time.sleep(4)
			print(f"{now_time()}", colored_green(f"Connected Token.. "))
			print(f"{now_time()}", colored_yellow(f"If you leave the tool, edge will close!"))
			print(f"{purple}>>>{end}  to exit print  15")
			main()

		except:
			print(colored_red_purple("Close, not installed or driver not up to date."))

	except Exception as e:
		print(f"Error:    {e}")