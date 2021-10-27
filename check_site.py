#!/usr/bin/env python3

import requests


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
	site_url = input("Enter website URL: ")

	response = check_site(site_url)
	if response == 200:
		print("site found: ", response)
	else:
		print("Error:", response)


if __name__ == "__main__":
	main()
