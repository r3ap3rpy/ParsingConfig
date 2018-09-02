from configparser import ConfigParser
import ast

class ConfigManager(object):
	def __init__(self, config_file):
		self.c = ConfigParser()
		self.c.read(config_file)

	@property
	def tiers(self):
		return self.c.sections()

	def get_tier(self, tier):
		if not tier in self.tiers:
			raise Exception('The specified tier is invalid!')

		return '{}\r\n{}'.format(self.c[tier]['Description'], ','.join(ast.literal_eval(self.c[tier]['systems'])))

	def get_tier_of_system(self, system):
		for tier in self.tiers:
			print('Checking tier: {}'.format(tier))
			if system in ast.literal_eval(self.c[tier]['systems']):
				return 'The systems is in tier: {}'.format(tier)
		else:
			raise Exception('The sepcified system {} is not a member of any tier!'.format(system))
				



if __name__ == '__main__':

	Manager = ConfigManager(config_file = 'test.cfg')

	print(Manager.tiers)

	print(Manager.get_tier('Development'))

	print(Manager.get_tier_of_system('k'))
