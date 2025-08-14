import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a !=n):
    
    a = int(input("Guess a numbe: "))
    if (a>n):
        print("Hint! - Enter lower number")
        guesses += 1
    elif(a<n):
        print("Hint! - Enter higher number")
        guesses += 1
print(f"You guessed the number {n} correct in {guesses} attempt")
