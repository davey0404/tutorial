print("Welcome to the Math Quiz!")

play = input("Do you want to start? ")

if play.lower() != "yes":
    quit()


print("Lets start: ")
score = 0


answer = input("What does 1 plus 1? ")
if answer == "2":
    print("First question correct!" )
    score += 1
else:
    print("First question wrong!")


answer = input("What does 2 plus 2? ")
if answer == "4":
    print("Second question correct!" )
    score += 1
else:
    print("Second question wrong!")

print("Total score is " + str(score))