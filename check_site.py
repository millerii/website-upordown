#!/usr/bin/env python3

import requests
from sys import argv


def check_site(url):
	try:
		response = requests.get(url)
	except requests.exceptions.ConnectionError:
		print("Address was not reachable")
	except requests.exceptions.MissingSchema:
		print("Invalid url-address")
	except requests.exceptions.RequestException as e:
		print("Other request problem: ", type(e), "\n", e)
	except Exception as e:
		print(type(e))
	else:
		# return HTTP-status code as int
		return response.status_code


def main():
	try:  # Check if url is provided as argument
		site_url = argv[1]
	except IndexError:
		site_url = input("Enter website URL: ")

	if not site_url.startswith("http"):  # Verify that url starts with 'http'
		print("URL entered without http or https prefix.")
		print("URL changed to", "https://" + site_url)
		site_url = "https://" + site_url

	response = check_site(site_url)
	if response == 200:
		print("*** Site found, response code:", response, "***")
	else:
		print("Error:", response)


if __name__ == "__main__":
	main()
