def vowel_count(s):
    
    VOWELS = "aeiouAEIOU"
    vc = 0
    for ch in s:
        if ch in VOWELS:
            vc += 1
    return vc
print(vowel_count("GFG is the best platform to learn from."))
