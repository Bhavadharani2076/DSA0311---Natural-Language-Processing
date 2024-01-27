#2
def is_match(input_string):
    # Define the finite state automaton transitions
    transitions = {
        0: {'a': 1, 'b': 0},
        1: {'a': 1, 'b': 2},
        2: {'a': 1, 'b': 0}
    }
    current_state = 0
    # Process each character in the input string
    for char in input_string:
        if char in transitions[current_state]:
            current_state = transitions[current_state][char]
        else:
            # If there is no transition for the current character, reset to the initial state
            current_state = 0
    # Check if the final state is reached
    return current_state == 2
# Test the automaton with various strings
test_strings = ["ab", "aab", "aaaab", "abc", "xyzab", "abab", "ba"]
for test_string in test_strings:
    if is_match(test_string):
        print(f"'{test_string}' matches the pattern.")
    else:
        print(f"'{test_string}' does not match the pattern.")
