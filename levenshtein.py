import difflib

word = "hello"
typos = ["hellp", "hellz"]

for typo in typos:
    seq = difflib.SequenceMatcher(None, word, typo)
    # Levenshtein distance approximation
    distance = int(round((1 - seq.ratio()) * max(len(word), len(typo))))
    print(f"Distance between '{word}' and '{typo}' is {distance}")
