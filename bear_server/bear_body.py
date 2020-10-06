import collections
import json

# Класс хранящий информацию по телу медведя
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
	# Метод для создание тела медведя в формате строки
	@staticmethod
	def create_bear_body(b_type, b_name, b_age, *args, **kwargs):
		config = BearBody()
		config.bear_type = b_type
		config.bear_name = b_name
		config.bear_age = b_age
		for i, k in zip(args[0::2], args[1::2]):
			setattr(config, i, k)
		for i in kwargs.keys():
			setattr(config, i, kwargs.get(i))
		return json.dumps(config.__dict__)
