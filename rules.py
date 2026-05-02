def leetspeak_variants(word):
    swaps = {
        "a": ["@", "4"],
        "e": ["3"],
        "i": ["!", "1"],
        "o": ["0"],
        "s": ["$", "5"],
        "t": ["7"]
    }

    variants = {word}

    for i, char in enumerate(word.lower()):
        if char in swaps:
            new_variants = set()

            for variant in variants:
                for replacement in swaps[char]:
                    new_variants.add(
                        variant[:i] + replacement + variant[i + 1:]
                    )

            variants.update(new_variants)

    return variants


def add_common_endings(word):
    endings = [
        "1", "12", "123", "!", "!!", "@", "#", "$",
        "2024", "2025", "2026", "69"
    ]

    return {word + ending for ending in endings}


def phrase_join_variants(phrase):
    words = phrase.strip().split()

    if len(words) <= 1:
        return {phrase}

    return {
        phrase,
        "".join(words),
        "_".join(words),
        "-".join(words),
        "!".join(words)
    }


def mutate_word(word, tier="light"):
    mutations = set()
    word = word.strip()

    if not word:
        return mutations

    if tier == "none":
        return {word}

    mutations.add(word)
    mutations.add(word.lower())
    mutations.add(word.upper())
    mutations.add(word.capitalize())

    if tier in ["medium", "heavy"]:
        current_mutations = list(mutations)

        for variant in current_mutations:
            mutations.update(leetspeak_variants(variant))
            mutations.update(add_common_endings(variant))

    if tier == "heavy":
        phrase_variants = phrase_join_variants(word)

        for phrase in phrase_variants:
            mutations.add(phrase)
            mutations.update(leetspeak_variants(phrase))
            mutations.update(add_common_endings(phrase))

        chained = set()

        for variant in list(mutations):
            for leet in leetspeak_variants(variant):
                chained.update(add_common_endings(leet))

        mutations.update(chained)

    return mutations