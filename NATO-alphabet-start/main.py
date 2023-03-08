import pandas

phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row1.letter: row1.code for (index, row1) in phonetic_df.iterrows()}


def phonetic():
    some = input("Enter a name: ")
    try:
        lt = [dictionary[n.upper()] for n in some]
    except KeyError:
        print("Sorry, only letters are allowed. Try again.")
        phonetic()
    else:
        print(f"Your list of phonetics for the given name: {lt}")


phonetic()
