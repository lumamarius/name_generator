from time import sleep

print("Welcome to the Generator!")
print("What is your Main Character?")
main_character = input("Main: ")
print(f"Cool! Your Main Character is {main_character}!")
user_name = input("Whats your Name? ")
print(f"Nice to meet you, {user_name}!")
sleep(3)
print(f"Your name could be {main_character} {user_name} or {user_name} {main_character}!")
sleep(3)
print("Yes, the Generator is really useless. Thanks for trying it out tho! :)")