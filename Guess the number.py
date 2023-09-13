import requests

# Api to get random number (1-10)
url = "https://random.org/integers/?num=1&min=1&max=10&base=10&col=1&format=plain"


repeat_answer = "Yes"

while repeat_answer.upper() == "YES":
    random_number = int(requests.get(url).text)
    counter = 0
    guess = 0
    print("Guess the number between 1-10 ")

    while random_number != guess:
        guess = int(input(">"))
        counter += 1
        if random_number == guess:
            print("You got it right!!")
            repeat_answer = input("Want to go again? (Type 'yes' to continue) ")
            break
        elif counter == 3:
            print("Game Over")
            repeat_answer = input("Want to go again? (Type 'yes' to continue) ")
            break
        elif guess < random_number:
            print("To low")
        elif guess > random_number:
            print("To high")
        else:
            break
print("Developed by Daan")
