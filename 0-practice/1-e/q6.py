# q6

# first function
def isLeagueUnited(hero1, hero2):
  if (hero1, hero2 == "Superman", "Wonder Woman"):
    print("True")
  else:
    print("False")

# second function
def decidePlan(hero1, hero2):
  isLeagueUnited(hero1, hero2)
  if (isLeagueUnited == "True"):
    print("Time to save the world!")
  else:
    print("We must unite the league!")

# third function
def run():

  print("Please enter the name of the first hero:")
  hero1 = str(input())

  print("Please enter the name of the second hero:")
  hero2 = str(input())

  print("Please enter league of plan:")
  response = str(input())

  if (response == "league"):
    isLeagueUnited(hero1, hero2)
  elif (response == "plan"):
    decidePlan(hero1, hero2)
  else:
    print("Invalid command. Please try again")

run()
