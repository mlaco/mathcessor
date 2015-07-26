__all__ = [ "word_to_number" ]


units = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

mults = {
    'thousand':    1000,
    'million':     1000000,
    'billion':     1000000000,
    'trillion':    1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion':  1000000000000000000000,
    'septillion':  1000000000000000000000000,
    'octillion':   1000000000000000000000000000,
    'nonillion':   1000000000000000000000000000000,
    'decillion':   1000000000000000000000000000000000,
}


def word_to_number(text):
    """All easy, except that "hundred" is special. 
    Four thousand three hundred is not 4 * 1000 * 3 * 100.
    """

    group_accum = 0  # reset to zero on close of every thousands
    whole_accum = 0

    for word in text.split():
        if word == "hundred":
            group_accum *= 100
            continue

        new_value = units.get(word)
        if new_value:
            group_accum += new_value
            continue

        multiplier = mults.get(word)
        if multiplier:
            whole_accum += group_accum * multiplier
            group_accum = 0  # reset
            continue

        raise ValueError(word)

    return whole_accum + group_accum
