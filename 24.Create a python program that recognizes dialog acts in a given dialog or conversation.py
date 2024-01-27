#24
import re

def recognize_dialog_acts(text):

    statements = re.compile(r'^[^?!.]*[.?!]$')
    questions = re.compile(r'.*\?$')
    greetings = re.compile(r'(hello|hi|hey).*', re.IGNORECASE)
    requests = re.compile(r'(please|can you|could you).*', re.IGNORECASE)

    utterances = re.split(r'[.?!]', text)

    dialog_acts = []
    for utterance in utterances:
        utterance = utterance.strip()
        if re.match(statements, utterance):
            dialog_acts.append((utterance, 'Statement'))
        elif re.match(questions, utterance):
            dialog_acts.append((utterance, 'Question'))
        elif re.match(greetings, utterance):
            dialog_acts.append((utterance, 'Greeting'))
        elif re.match(requests, utterance):
            dialog_acts.append((utterance, 'Request'))
        else:
            dialog_acts.append((utterance, 'Other'))

    return dialog_acts

conversation = "Hi! How are you? I'm fine, thank you. Can you pass the salt, please?"

recognized_acts = recognize_dialog_acts(conversation)
for utterance, act_type in recognized_acts:
    print(f"Utterance: '{utterance}', Dialog Act: {act_type}")
