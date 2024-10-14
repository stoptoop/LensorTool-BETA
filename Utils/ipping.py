import requests
import time
from .config import *










def ip_ping():
	try:
		def ping_ip(hostname, port, bytes):
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(2)
				start_time = time.time() 
				sock.connect((hostname, port))
				data = b'\x00' * bytes
				sock.sendall(data)
				end_time = time.time() 
				elapsed_time = (end_time - start_time) * 1000
				time.sleep(0.001)
				print(f'Hostname: {white}{hostname}{green} time: {white}{elapsed_time:.2f}ms{green} port: {white}{port}{green} bytes: {white}{bytes}{green} status: {white}succeed{green}')
			except:
				elapsed_time = 0
				print(f'Hostname: {white}{hostname}{red} time: {white}{elapsed_time}ms{red} port: {white}{port}{red} bytes: {white}{bytes}{red} status: {white}fail{red}')


		hostname = input(f"{now_time()}Ip ->  ")

		try:
			port_input = input(f"{now_time()}port (enter for default) ->  ")
			if port_input.strip():
				port = int(port_input)
			else:
				port = 80  
			
			bytes_input = input(f"{now_time()}Bytes (enter for default) ->  ")
			if bytes_input.strip():
				bytes = int(bytes_input)
			else:
				bytes = 64
		except:
			print(f"{purple}>>>{end}  to exit print  15")
			print("error restart program")

		while True:
			ping_ip(hostname, port, bytes)

	except Exception as e:
		print(f": ERROR as {e}")