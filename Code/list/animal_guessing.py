score = 0
wrong = 0
animals = [
    "cat", "dog", "cow", "tiger", "eagle", "elephant", "duck", 
    "whale", "fish", "horse", "pig", "goose", "zebra", "wolve",
    "rabbit", "rat", "mouse", "monkey", "turtle"]

animals_data = animals[:]

while True:
    guess = input("What animal you know? ")
    if guess == "\q":
        break

    is_correct = False
    index = 0
    for animal in animals:
        if animal.lower() == guess.lower():
            is_correct = True
            del animals[index]
            # animals.remove(guess)
            break
        index+=1

    if is_correct:
        score += 1
    else:
        wrong += 1
    
    print(f"Score: {score}")
    print(f"Wrong: {wrong}")
    # print(animals)
