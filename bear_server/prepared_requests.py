from bear_server import server_settings
from bear_server.end_points import *

import requests


# Класс с подготовленными запросами к API, методы возвращают ответы на запросы
class PreparedRequests:
	address = server_settings.Server.ADDRESS
	port = server_settings.Server.PORT

	headers = {"Content-type": server_settings.Header.CONTENT_TYPE, "Accept": server_settings.Header.CONTENT_TYPE}

	def createBear(self, bear_body):

		final_url = self.createURL() + EndPoints.BEAR

		response = requests.post(url=final_url, data=bear_body, headers=self.headers)

		return response

	def getAllBears(self):
		final_url = self.createURL() + EndPoints.BEAR

		response = requests.get(url=final_url, headers=self.headers)

		return response

	def getSpecificBear(self, idb):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		response = requests.get(url=final_url, headers=self.headers)

		return response

	def updateSpecificBear(self, idb, bear_body):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		response = requests.put(url=final_url, data=bear_body, headers=self.headers)

		return response

	def deleteSpecificBear(self, idb):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		response = requests.delete(url=final_url, headers=self.headers)

		return response

	def deleteAllBear(self):
		final_url = self.createURL() + EndPoints.BEAR

		response = requests.delete(url=final_url, headers=self.headers)

		return response

	def createURL(self):
		return "http://{}:{}".format(self.address, str(self.port))