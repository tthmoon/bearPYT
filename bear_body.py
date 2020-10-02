import collections
import json


class BearBody(collections.OrderedDict):

	class BearTypes:
		POLAR = "POLAR"
		BROWN = "BROWN"
		BLACK = "BLACK"
		GUMMY = "GUMMY"

	class Parameters:
		BEAR_TYPE = "bear_type"
		BEAR_NAME = "bear_name"
		BEAR_AGE = "bear_age"

	@staticmethod
	def create_bear_body(b_type, b_name, b_age, **kwargs):
		config = BearBody()
		config.bear_type = b_type
		config.bear_name = b_name
		config.bear_age = b_age
		for i in kwargs.keys():
			setattr(config, i, kwargs.get(i))
		return json.dumps(config.__dict__)
