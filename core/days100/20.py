from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask a few questions.")
print(f"What kind of computer are you learning to code on {user_name}?")
learning = input(prompt)

print(f"What is your favorite CPU {user_name}?")
cpu = input(prompt)

print("Do you have a GPU?")
gpu = input(prompt)

print(f"""
Alright, so your learing to code on a {learning}. 
Your favorite CPU is {cpu}, and I bet that will change soon.
You said {gpu}, about owning a GPU.
""")