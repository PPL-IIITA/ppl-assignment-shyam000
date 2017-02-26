from Q2boy import boy
from Q2girl import girl
class couple:
	def __init__ (self,boy,girl):
		self.boy = boy
		self.girl = girl
		self.happiness = 0
		self.compatability = 0
		self.intelligenceDiff = 0
		self.budgetDiff = 0
		self.attractivenessDiff = 0
	def set_happiness(self):
		self.happiness = self.boy.happiness + self.girl.happiness
	def set_compatability(self):
		self.budgetDiff = self.boy.budget - self.girl.maintainanceBudget
		self.intelligenceDiff = abs(self.boy.intelligence - self.girl.intelligence)
		self.attractivenessDiff = abs(self.boy.attractiveness - self.girl.attractiveness)
		self.compatability = self.budgetDiff + self.intelligenceDiff + self.attractivenessDiff
