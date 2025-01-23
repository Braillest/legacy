import louis

# louis.translateString(["braille-patterns.cti", "en-us-g2.ctb"], "Hello, World!")

filename = "War and Peace by graf Leo Tolstoy (564)"
text_path = f'./texts/{filename}'
braille_path = f'./braille/{filename}'
test_path = f'./test/{filename}'

# Input plaintext to grade 2 braille
with open(text_path, "r") as infile, open(braille_path, "w") as outfile:
    for line in infile.readlines():
        outfile.write(louis.translateString(["braille-patterns.cti", "en-us-g2.ctb"], line) + "\n")

# Grade 2 braille to plaintext output
with open(braille_path, "r") as infile, open(test_path, "w") as outfile:
    for line in infile.readlines():
        outfile.write(louis.backTranslateString(["braille-patterns.cti", "en-us-g2.ctb"], line)+ "\n")
