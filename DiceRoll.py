import random


print("\nWelcome to Dice rolling.")
while True:
    roll_dice = random.randint(1,6)
    roll = input("\nEnter to roll :")
    print(f"{roll_dice} rolled")

    roll_again = input("\nRoll again ? (yes/no):")
    if roll_again == 'yes':
      print("")
    elif roll_again == 'no':
     print("Goodbye!!")
     break
    else:
     print("\nEnter valid options.")
     break
