from bear_server import server_settings
from bear_server.end_points import *

from requests import Request


class PreparedRequests:
	address = server_settings.Server.ADDRESS
	port = server_settings.Server.PORT

	headers = {"Content-type": server_settings.Header.CONTENT_TYPE, "Accept": server_settings.Header.CONTENT_TYPE}

	def createBear(self, bear_body):

		final_url = self.createURL() + EndPoints.BEAR

		req = Request('POST', url=final_url, data=bear_body, headers=self.headers)

		return req.prepare()

	def getAllBears(self):
		final_url =self.createURL() + EndPoints.BEAR

		req = Request('GET', url=final_url, headers=self.headers)

		return req.prepare()

	def getSpecificBear(self, idb):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		req = Request('GET', url=final_url, headers=self.headers)

		return req.prepare()

	def updateSpecificBear(self, idb, bear_body):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		req = Request('PUT', url=final_url, data=bear_body, headers=self.headers)

		return req.prepare()

	def deleteSpecificBear(self, idb):
		final_url = self.createURL() + EndPoints.BEAR_SE.format(idb)

		req = Request('DELETE', url=final_url, headers=self.headers)

		return req.prepare()

	def deleteAllBear(self):
		final_url = self.createURL() + EndPoints.BEAR

		req = Request('DELETE', url=final_url, headers=self.headers)

		return req.prepare()

	def createURL(self):
		return "http://{}:{}".format(self.address, str(self.port))