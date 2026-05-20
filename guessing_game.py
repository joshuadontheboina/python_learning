secret_number=11
guess_attempt=0
guess_limit=3
while guess_attempt<guess_limit:
    guess=int(input("guess: "))
    guess+=1
    if guess==secret_number:
        print("you have won!!")
        break
else:
    print("sorry you've failed!")