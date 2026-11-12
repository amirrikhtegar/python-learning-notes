
if (words := ((sentence := input("pleas writing a sentence: ")).split())):
    count = len(words)
    print(f"Number of words in a sentence: {count}")
else:
    print("Please enter a valid sentence.")
