

def compute_patterns(inputs=None, pattern="new pattern"):
    if inputs is None:
        inputs = []
    inputs.append(pattern)
    patterns = ["a list based on "] + inputs
    print(patterns)

compute_patterns()


