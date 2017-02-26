class Girl:
	def __init__ (self,name,attractiveness,maintainanceBudget,Type,intelligence):
		self.name = name
		self.maintainanceBudget = maintainanceBudget
		self.Type = Type
		self.intelligence = intelligence
		self.happiness = 0
		self.bf = ''
		self.status = 'single'
		self.attractiveness = attractiveness

	def set_happiness(self,happiness):
		self.happiness = happiness
	def set_boyfriend(self,bf):
		self.bf = bf
	def isEligible(self,budget):
		if(self.maintainanceBudget <= budget):
			return True
		else:
			return False

