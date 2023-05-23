#https://www.hackerrank.com/challenges/30-inheritance

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg < 40:
            return 'T'
        elif 40<=avg<55:
            return 'D'
        elif 55<=avg<70:
            return 'P'
        elif 70<=avg<80:
            return 'A'
        elif 80<=avg<90:
            return 'E'
        elif 90<=avg<=100:
            return 'O'
            
firstName, lastName, idNum = input().split()
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)

s.printPerson()
print("Grade:", s.calculate())