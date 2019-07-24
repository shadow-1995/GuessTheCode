# PLEASE USE PYTHON# TO COMPILE THIS CODE
import random

class CodeGenerator:
	def __init__(self):
		self.length = random.randint(1,10)
		self.code = []
		self.getCode()
		self.guessedList=[]
		self.correctGuessed = []
	
	def getCode(self):  # generate random code 
		temp = 0
		while temp!=self.length:
			self.code.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
			temp+=1

	def checkCode(self,guess):  #filter function to check if both values are same or not and to maintain a list of values already parsed
		if guess[1][0] == guess[1][1] and (guess[0] not in self.guessedList):
			self.guessedList.append(guess[0])
			self.correctGuessed.append(guess[0])
			return True
		else:
			return False	
		
	def getPlayerInput(self,guessed): #check the guessed input
		del(self.guessedList[:])
		del(self.correctGuessed[:])
		correctPlaced = [x[1][1] for x in filter(self.checkCode,enumerate(zip(self.code,guessed)))]
		wrongPlaced = []
		for x in range(len(guessed)):
			for y in range(len(self.code)):
				if guessed[x] == self.code[y] and (y not in self.guessedList):
					self.guessedList.append(y)
					wrongPlaced.append(guessed[x])
		
		return (self.correctGuessed,wrongPlaced,correctPlaced)
		
	def AIInput(self): #generate Code of AI
		temp = 0
		AIcode = [] 
		while temp!=self.length:
			AIcode.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
			temp+=1
		return AIcode
		
	def guessAI(self,guess): # reguess the string based on previous result
		(correctIndex,wrongIndex,correct)=self.getPlayerInput(guess)
		print("AI Correct Postion Guessed %d Letters: %s"%(len(correct),''.join(correct)))
		print("AI Wrong Postion Guessed %d Letters %s:"%(len(wrongIndex),''.join(wrongIndex)))
		ascore=len(correctIndex)
		shuffleIndex= []
		for x in range(len(wrongIndex)):
			while True:
				randomNo = random.randrange(0,len(guess)-1)
				if (randomNo in correctIndex) and (randomNo in shuffleIndex):
					randomNo = random.randrange(0,len(guess)-1)
				else:
					break
			guess[randomNo] = wrongIndex[x]			
			shuffleIndex.append(randomNo)

		for x in range(len(guess)):
			if (x in correctIndex) or (x in shuffleIndex):
				continue
			guess[x] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		return guess,ascore	
	
	def getTries(self):
		x = int(self.length/2)
		if x < 3:
			return 3
		else:
			return x

def main():		
	t = CodeGenerator()
	x=0
	AI = t.AIInput()
	pScore = 0
	ascore = 0
	print("String Length: %d"%t.length)
	while x!=t.getTries():
		(c,wrongPlace,correctPlaced)=t.getPlayerInput(input("Player: ").upper())
		print("Player Correct Postion Guessed %d Letters: %s"%(len(correctPlaced),''.join(correctPlaced)))
		print("Player Wrong Postion Guessed %d Letters %s:"%(len(wrongPlace),''.join(wrongPlace)))
		pScore = len(correctPlaced)
		(AI,ascore)=t.guessAI(AI)
		x+=1
		if pScore == t.length:
			break
	print("Score Player: %d \t AI: %d"%(pScore,ascore))
	if pScore > ascore:
		print("Player Wins")
	elif ascore > pScore:
		print("AI wins")
	else:
		print("draw")
main()
