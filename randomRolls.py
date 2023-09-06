import random

def rollDice(amount: int = 2) -> list[int]:
    if amount < 0 :
        raise ValueError
    
    rolls: list[int] = []
    
    for i in range(amount):
        randomRoll: int = random.randint(1, 6)
        rolls.append(randomRoll)
        
    return rolls
    
    
def main():
    while True:
        try:
            userInput: str = input("Wie oft willst du würfeln?? ")
            
            if userInput.lower() == 'exit':
                print('Danke für das Spielen ')
                break
            
            print(rollDice(int(userInput)))
        except ValueError:
            print('Ich kann dich nicht verstehen')
            
            
if __name__== '__main__':
    main()