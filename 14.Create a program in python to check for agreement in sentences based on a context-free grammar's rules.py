#14
class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar
    def check_subject_verb_agreement(self, subject, verb):
        rules = self.grammar.get("S-V Agreement", [])
        for rule in rules:
            if rule[0] == subject and rule[1] == verb:
                return True
        return False
grammar = {
    "S-V Agreement": [
        ["dog", "barks"],
        ["dogs", "bark"],
        ["cat", "meows"],
        ["cats", "meow"]

    ]
}
agreement_checker = AgreementChecker(grammar)
subject = "dog"
verb = "barks"
is_agree = agreement_checker.check_subject_verb_agreement(subject, verb)

if is_agree:
    print(f"The subject '{subject}' and verb '{verb}' agree.")
else:
    print(f"The subject '{subject}' and verb '{verb}' do not agree.")
