def validator(input_str: str) -> bool:
    """Validates valid brackets for a string

    Args:
        input_str (str): [input string which may contain brackets]

    Returns:
        bool: [True | False]
    """
    tracker = {
    "{":0,
    "}":"{",
    "[":0,
    "]":"[",
    "(":0,
    ")":"("
    }
    list_of_brackets = []
    for lett in input_str:
        if lett in ["{", "[", "("]:
            list_of_brackets.append(lett)
        elif lett in ["}", "]", ")"]:
            if list_of_brackets and tracker[lett] == list_of_brackets[-1]:
                list_of_brackets.pop()
            else:
                return False

    return bool(list_of_brackets) == False

