#This program is meant to calculate the average of n numbers entered between the scale of
#0 to 4.3  and return the sum of the numbers divided by n for the average.

#isValidGrade is meant to return a True or False value if numbers entered are between 0 to 4.3
def isValidGrade(grade) :
   if grade >= 0 and grade <= 4.3 and grade == -1:
#return grade > 0 and grade = 4.3
       return "True"
   else:
       return "False"

#Function checks the validity of grade variable.
def getGrade() :
   grade = float(input("Enter a letter grade point value (or -1 to quit): "))
   #while (grade != -1 or not isValidGrade(grade)) :
   while (grade != -1 and not isValidGrade(grade)) :        #while loop will run as long as grade does not equal -1 and between 0 to 4.3
      print(grade, "is not valid.  A letter grade point value must be between 0 and 4.3.")      #Error Message display
      grade = float(input("Enter a letter grade point value (or -1 to quit): "))    #reprompts user for another grade value
   return grade

#Function that sums up valid numbers received, and adds value to the counter for the amount of numbers entered
def average() :
   grade = getGrade()
   sum = 0.0
   counter = 0
   #counter = 1
   while (grade != -1) :            # While numbers are valid, the while loop will add the numbers
      counter = counter + 1         # together and will also keep track of the amount of numbers entered.
      sum = sum + grade
#getGrade()
      grade = getGrade()
   return sum/counter               # returns the average value

print(average())                    # Displays the average value to the user
