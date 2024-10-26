from time import sleep

print("Willkommen zum Deadlock Name-Generator!")
print("Lass uns anfangen, welcher Charakter ist dein Main?")
main_character = input("Main: ")
print(f"Cool! Dein Main ist also {main_character}!")
user_name = input("Wie lautet dein echter Name? ")
print(f"Schön dich kennenzulernen {user_name}!")
sleep(3)
print(f"Dein Name könnte {main_character} {user_name} oder {user_name} {main_character} sein!")
sleep(3)
print("Ja, der Generator ist nicht wirklich hilfreich. Danke trotzdem fürs ausprobieren! :)")