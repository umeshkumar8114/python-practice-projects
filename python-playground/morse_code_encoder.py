# Translates input into Morse code using tuple mapping
morse = (
    ("A", ".-"), ("B", "-..."), ("C", "-.-."), ("D", "-.."), ("E", "."),
    ("F", "..-."), ("G", "--."), ("H", "...."), ("I", ".."), ("J", ".---"),
    ("K", "-.-"), ("L", ".-.."), ("M", "--"), ("N", "-."), ("O", "---"),
    ("P", ".--."), ("Q", "--.-"), ("R", ".-."), ("S", "..."), ("T", "-"),
    ("U", "..-"), ("V", "...-"), ("W", ".--"), ("X", "-..-"), ("Y", "-.--"), ("Z", "--.."),
)

morse_dict = dict(morse)

text = input("Enter text: ").upper()
for char in text:
    if char == " ":
        print(" ", end="")
    elif char in morse_dict:
        print(morse_dict[char], end=" ")
print()