print("Welcome to the Mad Libs generator!")

adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")
adjective3 = input("Enter the third adjective: ")
adjective4 = input("Enter the fourth adjective: ")

animal1 = input("Enter the name of an animal: ")
animal2 = input("Enter another animal name: ")
place = input ("Enter the name of the place: ")

if animal1.lower() == "monkey":
    monkey_activity = "swinging from the trees"
else:
    monkey_activity = f"doing something silly with a {animal1}"

if animal2.lower() == "Lion":
    lion_activity = "lounging in the sun"
else:
    lion_activity = f"doing something majestic like a {animal2}"

story = f"""
On a beautiful {adjective1} day, I went to the {place}.
I saw a funny {adjective2} {animal1} {monkey_activity}.
Then, I spotted a majestic {adjective3} {animal2} {lion_activity}.
What a wild and {adjective4} experience!
"""

print("\nHere's your Mad Libs story: ")
print(story)