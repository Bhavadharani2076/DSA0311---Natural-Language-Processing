#25
import random

def generate_text(prompt):
    responses = ["This is a simple response.", "Another generated text.", "A different response here."]
    return f"{prompt} {random.choice(responses)}"

while True:
    user_input = input("Enter a prompt (or 'exit' to end): ")
    
    if user_input.lower() == 'exit':
        print("Exiting.")
        break
