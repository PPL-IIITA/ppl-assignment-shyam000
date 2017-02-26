class Boy:
	def __init__ (self,name,attractiveness,reqAttractiveness,Type,intelligence,budget):
		self.name = name
		self.attractiveness = attractiveness
		self.reqAttractiveness = reqAttractiveness
		self.Type = Type
		self.intelligence = intelligence
		self.status = 'single'
		self.budget = budget
		self.gfName = ''
		self.happiness = 0
		self.gfBudget = 0


	def set_gf(self,gf):
		self.gfName = gf
	def changegfBudget(self,gfBudget):
		self.gfBudget = gfBudget
	def set_happiness(self,happiness) :
		self.happiness = happiness
	def isEligible(self,maintainanceBudget,attractiveness):
		if(self.budget >= maintainanceBudget) and (attractiveness >= self.reqAttractiveness):
			return True
		else:
			return False
