score = 0
wrong = 0
animals = [
    "cat", "dog", "cow", "tiger", "eagle", "elephant", "duck", 
    "whale", "fish", "horse", "pig", "goose", "zebra", "wolve",
    "rabbit", "rat", "mouse", "monkey", "turtle"]

while True:
    guess = input("What animal you know? ")
    if guess == "\q":
        break

    guess = guess.lower()
    if guess in map(str.lower, animals):
        score += 1
        animals.remove(guess)
    else:
        wrong += 1
    
    print(f"Score: {score}")
    print(f"Wrong: {wrong}")
