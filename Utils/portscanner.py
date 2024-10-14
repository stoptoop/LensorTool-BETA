import requests
from .config import *




def port_scanner_func():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	try:
		def port_scanner(ip):
			port_protocol_map = {
				21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
				80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
				443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
				1521: "Oracle DB", 3389: "RDP", 1900: "SSDP"
			}

			def scan_port(ip, port):
				try:
					now_sock = datetime.now()
					current_time_sock = now_sock.strftime("%H:%M:%S")
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.settimeout(0.1)
					result = sock.connect_ex((ip, port))
					if result == 0:
						protocol = identify_protocol(ip, port)
						print(f"{now_time()}", colored_green(f"Port: {port} Status: Open Protocol: {protocol}"))
					sock.close()
				except:
					pass

			def identify_protocol(ip, port):
				try:
					if port in port_protocol_map:
						return port_protocol_map[port]
					else:
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sock.settimeout(0.5)
						sock.connect((ip, port))
						
						sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
						response = sock.recv(100).decode('utf-8')
						if "HTTP" in response:
							return "HTTP"
						
						sock.send(b"\r\n")
						response = sock.recv(100).decode('utf-8')
						if "FTP" in response:
							return "FTP"
						
						sock.send(b"\r\n")
						response = sock.recv(100).decode('utf-8')
						if "SSH" in response:
							return "SSH"
						return "Unknown"
					
				except:
					return "Unknown"


			with concurrent.futures.ThreadPoolExecutor() as executor:
				results = {executor.submit(scan_port, ip, port): port for port in range(1, 65535 + 1)}
			concurrent.futures.wait(results)



		def is_valid_ip(ip):
			try:
				ipaddress.ip_address(ip)
				return True
			except ValueError:
				return False
			
		def is_ip_reachable(ip):
			try:
				response = ping(ip, timeout=2)
				return response is not None
			except Exception as e:
				print(f"Error: {e}")
				return False


		ip = input(f"{now_time()} ~ Insert Ip ~ {purple}[ {end}> {purple}]  {end}")
		input_without_dots = ip.replace('.', '')




		if is_valid_ip(ip):
			if is_ip_reachable(ip):
				print(f"{now_time()}", colored_yellow(f"Start Scanning...                          Restart the program to stop"))
				port_scanner(ip)
			else:
				print(f"{now_time()}", colored_red_purple(f"IP address unavailable"))
				port_scanner_func()
		elif ip == "15":
			banner()
			main()
		else:
			print(f"{now_time()}", colored_red_purple(f"Something went wrong please check your input"))
			port_scanner_func()



		# if input_without_dots.isdigit():
		# 	print(f"{purple}[ {end}{current_time} {purple}] {end}", colored_yellow(f"Start Scanning...                          Restart the program to stop"))
		# 	port_scanner(ip)

		# else:
		# 	print(f"{purple}[ {end}{current_time} {purple}] {end}", colored_red_purple(f"Something went wrong please check your input"))
		# 	port_scanner_func()
		# print()

	except Exception as e:
		print(e)